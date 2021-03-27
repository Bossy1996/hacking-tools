#! /usr/bin/python

from socket import *
import optparse # technically i can avoid this library using  click 
from threading import *
import click

def conScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        


def portScan(tgtHost, tgtPorts):
    try:
        tgtIp = gethostbyname(tgtHost)
    except:
        print("Unknown host %s" %tgtHost)
    
    try:
        tgtName = gethostbyaddr(tgtIp)
        print("[*] Scan results for: " + tgtName[0])
    except:
        print("[*] Scan  results for " + tgtIp)
    
    setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        t = Thread(target=conScan, args=(tgtHost, int(tgtPort)))
        t.start()

def main():
    parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target port>')
    parser.add_option("-H", dest='tgtHost', type='string', help='specify target host')
    parser.add_option("-p", dest='tgtPort', type='string', help='specify target ports separated by coma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')

    if tgtHost == None | tgtPorts[0] == None:
        print(parser.usage)
        exit(0)
    
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()