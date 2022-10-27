from socket import *


serverName = ('127.0.0.1', 10000)
clientSocket = socket(AF_INET, SOCK_STREAM)

bufferSize = 16
#myFile = input(__prompt= "what do you want to send?")
myFile = bytearray(b'\x12\x1B\x03')
clientSocket.bind((serverName))


#while (myFile.length):
 #   clientSocket.sendto(myFile, (serverName, clientSendPort))
  #  addr = clientSocket.recvfrom(bufferSize)
   # print(addr)
message = bytearray(0)
try:
    clientSocket.sendall(myFile)

    while True:
        data = sock.recv(bufferSize)
        if data == bytearray(b'\x13\x37'):
            break
        print( "got some data")
finally:
    clientSocket.close()


