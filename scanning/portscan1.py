#! /usr/bin/python

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP PACKAGE

# if after 2 sec it doen't give a response the port is closed
socket.setdefaulttimeout(2)

try:   
    host = str(input("[*] Enter the host to scan: "))
except ValueError:
    print("Value Error!")

def portscanner(port):
    if sock.connect_ex((host, port)):
        print("Port %d is closed" %(port))
    else:
        print("Port %d is open" %(port))

for port in range(100):
    portscanner(port)

