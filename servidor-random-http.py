#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import random
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)  
num = random.randint(0,9999999)
try: 
	while True:
		num = random.randint(0,9999999)
		print 'Escriba en el navegador localhost:1234'
		print 'Waiting for connections'
		(recvSocket, address) = mySocket.accept()
		print 'Request received:'
		print recvSocket.recv(2048)
		print 'Answering back...'
		recvSocket.send("HTTP/1.1 200 Ok \r\n\r\n" + "<html><body><h1>Hola.</h1>"  + "<a href= ' " + str(num) + "' >Dame otra<a/>" +"</p>" + "</body></html> \r\n")
		
		recvSocket.close()
except KeyboardInterrupt:
	print "Closing binded socket"
	mySocket.close()
