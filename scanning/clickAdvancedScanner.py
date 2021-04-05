#! /usr/bin/python3

from socket import *
from threading import *
import click
import sys


def portScan(tgtHost, tgtPort):
    try:
        tgtIp = gethostbyname(tgtHost)
    except:
        print("Unknown host %s" %tgtHost)

    try:
        tgtName = gethostbyaddr(tgtIp)


@click.command()
@click.option('--host', required=True ,type=str, help='specify target host.',)
@click.option('--port', type=str, help='specify target ports separated by comas.')
def main(host, port):
    tgtHost = host
    tgtPort = port.split(',')
    portScan(tgtHost, tgtPort)

if __name__ == '__main__':
    main() 
    
