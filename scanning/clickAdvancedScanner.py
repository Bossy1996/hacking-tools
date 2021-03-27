#! /usr/bin/python3

from socket import *
from threading import *
import click
import sys


@click.command()
@click.option('--host', required=True ,type=str, help='specify target host.',)
@click.option('--port', type=str, help='specify target ports separated by comas.')
def main(host, port):
    tgtHost = host
    tgtPort = port.split(',')

    portScan(tgtHost, tgtPort)

if __name__ == '__main__':
    main() 
    
