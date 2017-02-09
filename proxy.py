###########################################
##            Nikko Williard             ##
##               CSEC-380                ##
##   Rochester Institute of Technology   ##
##          Prof. Chaim Sanders          ##
##           February 9, 2017            ##
###########################################

import urllib.request
import socket
import struct


def proxy(start, stop):
    start = struct.unpack(">L", socket.inet_aton(start))[0]
    stop = struct.unpack(">L", socket.inet_aton(stop))[0]
    twohundo = []

    while start <= stop:
        print("IP: http://%s" % socket.inet_ntoa(struct.pack(">L", start)))
        try:
            proxyhandler = urllib.request.ProxyHandler({"http": "http://%s" % socket.inet_ntoa(struct.pack(">L", start))})
            builder = urllib.request.build_opener(proxyhandler)
            open = builder.open("http://chaimsanders.com", timeout=3)
            code = open.getcode()
            page = open.read()
            if code == 200:
                twohundo.append("http://%s" % socket.inet_ntoa(struct.pack(">L", start)))
                print("Code: ", code)
                print("Content: ", page, "\n")
            else:
                print(code)
                pass
        except urllib.request.URLError:
            print("No response at: http://%s" % socket.inet_ntoa(struct.pack(">L", start)), "\n")
        start += 1
    print("List of 200's: ", twohundo)
    print("Now go have fun.")

proxy("92.110.98.125", "92.110.98.126")
