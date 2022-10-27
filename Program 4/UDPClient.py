from socket import *
import packets
import pickle
import tkinter
image = "testfile.bmp"

# open image
bufferSize = 2048
bufferExt = 16*3
myfile = open(image, 'rb')
sequenceNumber = 0
totalBytes = 0



serverName = '127.0.0.1'
serverSendPort = 12000
serverSendPort = int(serverSendPort)
serverListenPort = 12001
clientSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind((serverName, serverListenPort))


def timeout():
    clientSocket.sendto(dataSend,(serverName, serverSendPort))
    timerObject = emptyObject.after(50, timeout)
    
emptyObject = tkinter.Button()

while (1):
    if (sequenceNumber == 0):
        data = myfile.read(bufferSize) #getting data from file
        data = packets.mkepckt(data, 0, packets.calculateChecksum(data, bufferSize)) #creating a tuple packet
        dataSend = pickle.dumps(data)
        clientSocket.sendto(dataSend,(serverName, serverSendPort))
        timerObject = emptyObject.after(50, timeout)
        sequenceNumber = 1
        
        
        ACK, addr = serverSocket.recvfrom(bufferSize + bufferExt)
        ACK = pickle.loads(ACK)
        ACKchecksum = packets.calculateChecksum(ACK[1], len(ACK[1])) #1 is data, 

        while (1): # 2 is checksum
           
            
            ACK, addr = serverSocket.recvfrom(bufferSize + bufferExt)
            ACK = pickle.loads(ACK)
            ACKchecksum = packets.calculateChecksum(ACK[1], len(ACK[1])) #1 is data, 

            if(ACK[0] is not 0 or ACKchecksum is not ACK[2]):
                break
        timerObject.after_cancel()
    elif (sequenceNumber == 1):
        data = myfile.read(bufferSize)
        data = packets.mkepckt(data, 1, packets.calculateChecksum(data, bufferSize))
        dataSend = pickle.dumps(data)
        clientSocket.sendto(dataSend,(serverName, serverSendPort))
        timerObject = emptyObject.after(50, timeout)
        sequenceNumber = 0
    
        ACK, addr = serverSocket.recvfrom(bufferSize + bufferExt)
        ACKchecksum = packets.checksum(ACK[1], len(ACK[1]))

        while (1):
            clientSocket.sendto(dataSend, (serverName, serverSendPort))
            ACK, addr = serverSocket.recvfrom(bufferSize + bufferExt)
            ACK = pickle.loads(ACK)
            ACKchecksum = packets.calculateChecksum(ACK[1], len(ACK[1]))

            if(ACK[0] is not 1 or ACKchecksum is not ACK[2]):
                break
        timerObject.after_cancel()


myfile.close()


clientSocket.close()
serverSocket.close()