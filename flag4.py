import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("54.209.150.110", 80))

# Token Request
getSecure = "POST /getSecure HTTP/1.1\n" \
            "Host: 54.209.150.110\n" \
            "Authorization: 41ee472be69964f80d430e067842f045b26699a23cc9d34cee0c95e8\n\n"

sock.send(getSecure.encode())
secureData = sock.recv(1024)
sock.close()
sd = secureData.decode("utf-8")
token = sd.split(':')[8].strip('\"').strip()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("54.209.150.110", 80))

# Eval Request
getFlag4 = "POST /createAccount HTTP/1.1\n" \
           "Host: 54.209.150.110\n" \
           "Accept: */*\n" \
           "Accept-Encoding: gzip,deflate\n" \
           "Accept-Language: en\n" \
           "Content-Length: 78\n" \
           "User-Agent: Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko\n" \
           "Content-Type: application/x-www-form-urlencoded\n\n" \
           "token=%s&username=edmead" \
           % token

sock.send(getFlag4.encode())
secureData = sock.recv(1024)
sock.close()
sd = secureData.decode("utf-8")
print(sd)
password = sd.split(' ')[-1].strip('\"').strip()
password = password.replace('&', '%26').replace('=','%3D')
length = 88 + len(str(password))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("54.209.150.110", 80))

# Login Request
getFlag4pass = "POST /login HTTP/1.1\n" \
               "Host: 54.209.150.110\n" \
               "Accept: */*\n" \
               "Accept-Encoding: gzip,deflate\n" \
               "Accept-Language: en\n" \
               "Content-Length: %d\n" \
               "User-Agent: Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko\n" \
               "Content-Type: application/x-www-form-urlencoded\n\n" \
               "token=%s&username=edmead&password=%s" \
               % (length, token, password)

sock.send(getFlag4pass.encode())
secureData = sock.recv(1024)
sock.close()
sd = secureData.decode("utf-8")
print(sd)

# FLAG1: 388ab48da65ef7860a2751589742866393ca47900e311973c17dece1
# FLAG2: 16b2eb06559c2e4bd1ba03c3a7600a1feb5d11e06421e27f43111659
# FLAG3: 41ee472be69964f80d430e067842f045b26699a23cc9d34cee0c95e8
# FLAG4: a68cec27e3717a91aa89b554f941f7b0c121c1d01e0014bbed2202a3
