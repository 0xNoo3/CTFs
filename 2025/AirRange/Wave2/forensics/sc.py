import base64
from scapy.all import *

packets = rdpcap("gatekeepers_secret.pcap")
hidden_data = []

for pkt in packets:
    if IP in pkt:
        ip_id = pkt[IP].id
        # Filter based on sender or specific protocol, if needed
        hidden_data.append(ip_id)

# Convert to ASCII if they seem to be character codes
answer = "".join([chr(i) for i in hidden_data if 32 <= i <= 126])

print(answer)

encoded = "MZWGCZ33OVPXEX2GGBZDG3TTGFRXGX2LGFXGO7I="
decoded = base64.b32decode(encoded)

# Print as printable ASCII, replace non-printables with '.'
printable = ''.join(chr(c) if 32 <= c <= 126 else '.' for c in decoded)
print(printable)
