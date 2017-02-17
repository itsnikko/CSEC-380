import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("54.209.150.110", 80))

# Token Request
getSecure = b"""
POST /getSecure HTTP/1.1
Host: 54.209.150.110
Authorization: 16b2eb06559c2e4bd1ba03c3a7600a1feb5d11e06421e27f43111659\r\n\r\n
"""

sock.send(getSecure)
secureData = sock.recv(1024)
sock.close()
sd = secureData.decode("utf-8")
token = sd.split(':')[8].strip('\"').strip()
print("Token is: %s" % token)
print(len("token=%s" % token))
btoken = token.encode()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("54.209.150.110", 80))

# Eval Request
getFlag3 = b"""
POST /getFlag3Challenge HTTP/1.1
Host: 54.209.150.110
Content-Length: 62
Content-Type: application/x-www-form-urlencoded\n
token=%b
""" % btoken

sock.send(getFlag3)
secureData = sock.recv(1024)
sock.close()
sd = secureData.decode("utf-8")
print(sd)

solution = sd.split(':')[8].strip('\"').strip()
sol = eval(solution)
length = 62 + 10 + len(str(sol))

# Challenge Request
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("54.209.150.110", 80))

captcha = "POST /getFlag3Challenge HTTP/1.1\n" \
          "Host: 54.209.150.110\n" \
          "Content-Length: %d\n" \
          "Content-Type: application/x-www-form-urlencoded\n\n" \
          "token=%s&solution=%s"\
          % (length, token, sol)

print(captcha.encode())

sock.send(captcha.encode())
secureData = sock.recv(1024)
sock.close()
sd = secureData.decode("utf-8")
print(sd)

# FLAG1: 388ab48da65ef7860a2751589742866393ca47900e311973c17dece1
# FLAG2: 16b2eb06559c2e4bd1ba03c3a7600a1feb5d11e06421e27f43111659
# FLAG3: 41ee472be69964f80d430e067842f045b26699a23cc9d34cee0c95e8
# FLAG4: a68cec27e3717a91aa89b554f941f7b0c121c1d01e0014bbed2202a3
