#!/usr/bin/python
# Ejercicio 14.3 Aplicacion Web generadora de URLs aleatorias
# Christian Bermejo Guerrero

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

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

while True:
    print ('Waiting for connections')
    (recvSocket, address) = mySocket.accept()
    print ('HTTP request received:')
    print (recvSocket.recv(1024))
    randomURL = random.randint(1,99999999)
    recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                    "<html><body><h1>Hola.</h1></body></html>\r\n","utf-8"))
    # PYTHON 3
    # bytes fix--> a bytes-like object is required, not str
    # utf-8 fix--> string argument without encoding
    recvSocket.send(bytes("<h1><A HREF=" + str(randomURL) +
                          ">Dame Otra</h1></A>", "utf-8"))
    recvSocket.close()
