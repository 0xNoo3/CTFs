b *0x5555555553D5  # <- wherever decryption finishes
commands
    x/s $rsp+0x30
    quit
end
run
