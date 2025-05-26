# dump.gdb
set pagination off

# 1) Break right after FUN_0x32a returns
break *0x5555555553C9

commands
  silent
  printf "\n[+] Decrypted in-memory flag:\n"
  x/s $rbp-0x60
  quit
end

run
