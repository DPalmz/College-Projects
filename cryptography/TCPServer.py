from socket import *

serverAddress = ('127.0.0.1', 10000)
serverListenSocket = socket(AF_INET, SOCK_STREAM)
serverListenSocket.bind((serverAddress))

bufferSize = 16

send = bytearray(b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x10')

print("ready to receive")
while (1):
    print("waiting for connection")
    connection, addr = serverListenSocket.accept()
    try:
        while (1):
            data = connection.recv(bufferSize)
            if (data):
                 connection.sendall(send)
            else:
                print("no more data")
                break

    finally:
        send = bytearray(b'\x13\x37')
        connection.sendall(data)
        connection.close()
