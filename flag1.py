import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("54.209.150.110", 80))

getSecure = b"""
POST / HTTP/1.1
Host: 54.209.150.110\r\n\r\n
"""

sock.send(getSecure)
secureData = sock.recv(1024)
sock.close()
sd = secureData.decode("utf-8")
print(sd)

# FLAG1: 388ab48da65ef7860a2751589742866393ca47900e311973c17dece1
# FLAG2: 16b2eb06559c2e4bd1ba03c3a7600a1feb5d11e06421e27f43111659
# FLAG3: 41ee472be69964f80d430e067842f045b26699a23cc9d34cee0c95e8
# FLAG4: a68cec27e3717a91aa89b554f941f7b0c121c1d01e0014bbed2202a3
