from libdebug import debugger
from pwn import *

known_flag = b"utflag{1_w4nna_pl4y_hypix3l_in_c}"
to_skip = len(known_flag)
while len(known_flag) != 0x21:
    found = False
    possible_chars = []
    for i in range(33,128):
        d = debugger("./safeWord")
        pipe = d.run()
        pipe.sendline(known_flag + ((0x21 - len(known_flag)) * p8(i)))
        d.breakpoint(0x133C9,file="binary",hardware=False)
        d.cont()
        for k in range(to_skip):
            d.cont()
        inst = hex(d.regs.rdi)[2:]
        if inst[:4] == "c358" and inst[6:8] == "6a": #ugly way to verify 
            #inst is valid, continue
            possible_chars.append(p8(i))
            found = True
        else:
            d.kill()
    if possible_chars:
        known_flag += possible_chars[0]
        to_skip += 1
    print(possible_chars)
    if found == False:
        print("failed")