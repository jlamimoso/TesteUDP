#!/usr/bin/env python

import socket
import sys

UDP_IP = "0.0.0.0"
UDP_PORT = 9090

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT))

print >> sys.stderr, "Iniciando servidor na porta %s " % UDP_IP

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print >> sys.stderr, "Received message: %s from %s" % (data, addr)