#!/usr/bin/python

file = open("chal.ashfaq", "r")
diss_vm = open("asm.txt" , "w")
content = file.read()
vmdump = bytes.fromhex(content)


vm_pc = 0


