#!/usr/bin/python

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket
import random
# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))

mySocket.listen(5)
num = random.randint(0,9999999)
# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)
try:
    while True:
        num = random.randint(0,9999999)
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'HTTP request received:'
        print recvSocket.recv(1024)
        recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><body><h1>Hola! Eres de esta IP (" + str(address[0]) + 
                        ") y de este puerto (" + str(address[1]) + ") " +
                        "<a href= ' " + str(num) + " ' >Dame una URL<a/>" +"</p>" +
                        "</body></html>" + "\r\n")
                        
        recvSocket.close()
except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()
