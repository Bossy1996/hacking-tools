#! /usr/bin/python

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP PACKAGE
try:   
    host = str(input("[*] Enter the host to scan: "))
except ValueError:
    print("Value Error!")
try:
    port = int(input("[*] Enter the port to scan: "))
except ValueError:
    print("Value Error, it must be an integer!")

def portscanner(port):
    if sock.connect_ex((host, port)):
        print("Port %d is closed" %(port))
    else:
        print("Port %d is open" %(port))

portscanner(port)

