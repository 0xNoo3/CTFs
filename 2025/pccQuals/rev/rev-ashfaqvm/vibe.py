#!/usr/bin/python3

# Simple, clear disassembler for the ashfaq VM
# - Reads chal.ashfaq (hex-encoded bytecode)
# - Decodes instructions and operands
# - Writes human-readable listing to asm.txt

from typing import Tuple


def read_file_bytes_hex(path: str) -> bytes:
	# Read as binary; if the content consists only of hex digits and whitespace, treat it as hex text.
	with open(path, "rb") as f:
		data = f.read()
	# Check if all bytes are hex-digit or whitespace
	HEXWS = b"0123456789abcdefABCDEF \t\r\n"
	if data and all(b in HEXWS for b in data):
		content = data.decode("ascii").strip()
		if content:
			return bytes.fromhex(content)
	# Fallback: return raw bytes
	return data


def u8(b: bytes, off: int) -> Tuple[int, int]:
	return b[off], off + 1


def u16(b: bytes, off: int) -> Tuple[int, int]:
	return int.from_bytes(b[off:off+2], "little"), off + 2


def u32(b: bytes, off: int) -> Tuple[int, int]:
	return int.from_bytes(b[off:off+4], "little"), off + 4


def reg_name(r: int) -> str:
	return f"R{r}"


def fmt_imm32(x: int) -> str:
	return f"0x{x:08X}"


def fmt_imm8(x: int) -> str:
	return f"0x{x:02X}"


def disassemble(input_hex_path: str, output_asm_path: str) -> None:
	code = read_file_bytes_hex(input_hex_path)
	n = len(code)
	pc = 0

	with open(output_asm_path, "w") as out:
		def w(line: str):
			out.write(line + "\n")

		while pc + 1 < n:
			insn_pc = pc
			opcode, pc = u16(code, pc)

			# Map opcodes
			if opcode == 0xDEAD:
				w(f"0x{insn_pc:04X}: HALT")
				# continue

			elif opcode == 0xFFFF:
				# Extended, run-time R1-based action
				w(f"0x{insn_pc:04X}: EXT    ; runtime action based on R1 (1=READ,2=WRITE,3=STRLOAD,4=DUMPREG,5=DUMPSTK,6=DUMPSTR,255=EXIT)")

			elif opcode == 0x9900:
				# CMP Rdst, imm32|Rsrc
				if pc + 1 + 4 + 1 > n:
					w(f"0x{insn_pc:04X}: CMP    ; truncated")
					break
				dst, pc = u8(code, pc)
				val, pc = u32(code, pc)
				flag, pc = u8(code, pc)
				if flag:
					w(f"0x{insn_pc:04X}: CMP    {reg_name(dst)}, {reg_name(val & 0xFF)}")
				else:
					w(f"0x{insn_pc:04X}: CMP    {reg_name(dst)}, {fmt_imm32(val)}")

			elif 0x99A0 <= opcode <= 0x99A6:
				# Conditional jumps (absolute PC target in next 16-bit)
				if pc + 2 > n:
					w(f"0x{insn_pc:04X}: J??    ; truncated target")
					break
				target, pc = u16(code, pc)
				mnem = {
					0x99A0: "JMP",
					0x99A1: "JZ",
					0x99A2: "JNZ",
					0x99A3: "JG",
					0x99A4: "JGE",
					0x99A5: "JL",
					0x99A6: "JLE",
				}[opcode]
				w(f"0x{insn_pc:04X}: {mnem:<5}  0x{target:04X}")

			elif opcode == 0x0C00 or opcode == 0x0C01:
				# REGMOVE/REGCOPY Rd, Rs (2 bytes: dst, src)
				if pc + 2 > n:
					w(f"0x{insn_pc:04X}: REG??? ; truncated")
					break
				dst, pc = u8(code, pc)
				src, pc = u8(code, pc)
				mnem = "REGCOPY" if opcode == 0x0C01 else "REGMOVE"
				w(f"0x{insn_pc:04X}: {mnem:<7} {reg_name(dst)}, {reg_name(src)}")

			elif opcode == 0x0C02:
				# MOVI Rd, imm32
				if pc + 1 + 4 > n:
					w(f"0x{insn_pc:04X}: MOVI   ; truncated")
					break
				dst, pc = u8(code, pc)
				imm, pc = u32(code, pc)
				w(f"0x{insn_pc:04X}: MOVI   {reg_name(dst)}, {fmt_imm32(imm)}")

			elif opcode == 0x0D00:
				# PUSH imm32|Rsrc (imm32 + flag8)
				if pc + 4 + 1 > n:
					w(f"0x{insn_pc:04X}: PUSH   ; truncated")
					break
				val, pc = u32(code, pc)
				flag, pc = u8(code, pc)
				if flag:
					w(f"0x{insn_pc:04X}: PUSH   {reg_name(val & 0xFF)}")
				else:
					w(f"0x{insn_pc:04X}: PUSH   {fmt_imm32(val)}")

			elif opcode == 0x0D01:
				# POP Rd (1 byte)
				if pc + 1 > n:
					w(f"0x{insn_pc:04X}: POP    ; truncated")
					break
				dst, pc = u8(code, pc)
				w(f"0x{insn_pc:04X}: POP    {reg_name(dst)}")

			elif opcode == 0x0D02:
				# PEEK Rd (1 byte)
				if pc + 1 > n:
					w(f"0x{insn_pc:04X}: PEEK   ; truncated")
					break
				dst, pc = u8(code, pc)
				w(f"0x{insn_pc:04X}: PEEK   {reg_name(dst)}")

			elif 0x0F00 <= opcode <= 0x0F07:
				# ALU Rdst, imm32|Rsrc (dst8, imm32, flag8)
				if pc + 1 + 4 + 1 > n:
					w(f"0x{insn_pc:04X}: ALU    ; truncated")
					break
				dst, pc = u8(code, pc)
				val, pc = u32(code, pc)
				flag, pc = u8(code, pc)
				mnem = {
					0x0F00: "ADD",
					0x0F01: "SUB",
					0x0F02: "OR",
					0x0F03: "AND",
					0x0F04: "XOR",
					0x0F05: "MUL",
					0x0F06: "DIV",
					0x0F07: "MOD",
				}[opcode]
				if flag:
					w(f"0x{insn_pc:04X}: {mnem:<5} {reg_name(dst)}, {reg_name(val & 0xFF)}")
				else:
					w(f"0x{insn_pc:04X}: {mnem:<5} {reg_name(dst)}, {fmt_imm32(val)}")

			elif opcode == 0x0F08 or opcode == 0x0F09:
				# SHL/SHR Rdst, imm8|Rsrc (dst8, val8, flag8)
				if pc + 3 > n:
					w(f"0x{insn_pc:04X}: SH?    ; truncated")
					break
				dst, pc = u8(code, pc)
				val8, pc = u8(code, pc)
				flag, pc = u8(code, pc)
				mnem = "SHL" if opcode == 0x0F08 else "SHR"
				if flag:
					w(f"0x{insn_pc:04X}: {mnem:<5} {reg_name(dst)}, {reg_name(val8)}")
				else:
					w(f"0x{insn_pc:04X}: {mnem:<5} {reg_name(dst)}, {fmt_imm8(val8)}")

			elif opcode == 0x5A0:
				# STR.ADD uid, len, [len bytes inline]
				if pc + 1 + 4 > n:
					w(f"0x{insn_pc:04X}: STR.ADD ; truncated")
					break
				length, pc = u8(code, pc)
				uid, pc = u32(code, pc)
				# Inline bytes
				if pc + length > n:
					data = code[pc:n]
					pc = n
				else:
					data = code[pc:pc+length]
					pc += length
				hex_bytes = " ".join(f"{b:02X}" for b in data)
				w(f"0x{insn_pc:04X}: STR.ADD {fmt_imm32(uid)}, {length}    ; {hex_bytes}")

			elif opcode == 0x5B0:
				# STR.LOAD uid -> buffer
				if pc + 4 > n:
					w(f"0x{insn_pc:04X}: STR.LOAD ; truncated")
					break
				uid, pc = u32(code, pc)
				w(f"0x{insn_pc:04X}: STR.LOAD {fmt_imm32(uid)}")

			elif opcode == 0x5B1:
				# STR.SAVE uid <- buffer
				if pc + 4 > n:
					w(f"0x{insn_pc:04X}: STR.SAVE ; truncated")
					break
				uid, pc = u32(code, pc)
				w(f"0x{insn_pc:04X}: STR.SAVE {fmt_imm32(uid)}")

			elif opcode == 0x5B2:
				# BUFLD R1, idx(imm8|Rsrc) (2 bytes: val8, flag8)
				if pc + 2 > n:
					w(f"0x{insn_pc:04X}: BUFLD  ; truncated")
					break
				val8, pc = u8(code, pc)
				flag, pc = u8(code, pc)
				if flag:
					w(f"0x{insn_pc:04X}: BUFLD  R1, {reg_name(val8)}")
				else:
					w(f"0x{insn_pc:04X}: BUFLD  R1, {fmt_imm8(val8)}")

			elif opcode == 0x5B3:
				# STRIDX R1, uid, idx(imm8|Rsrc)  (uid32, idx8, flag8)
				if pc + 4 + 2 > n:
					w(f"0x{insn_pc:04X}: STRIDX ; truncated")
					break
				uid, pc = u32(code, pc)
				idx, pc = u8(code, pc)
				flag, pc = u8(code, pc)
				if flag:
					w(f"0x{insn_pc:04X}: STRIDX R1, {fmt_imm32(uid)}, {reg_name(idx)}")
				else:
					w(f"0x{insn_pc:04X}: STRIDX R1, {fmt_imm32(uid)}, {fmt_imm8(idx)}")

			else:
				w(f"0x{insn_pc:04X}: INVALID 0x{opcode:04X}")

if __name__ == "__main__":
	disassemble("chal.ashfaq", "asm.txt")