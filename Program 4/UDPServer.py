from socket import *
import packets
import pickle
image = "image%s.bmp"

serverListenPort = 12000
serverSendPort = 12001
clientName = '127.0.0.1'
serverListenSocket = socket(AF_INET, SOCK_DGRAM)
serverListenSocket.bind(('127.0.0.1', serverListenPort))
serverSendSocket = socket(AF_INET, SOCK_DGRAM)

print("The server is ready to receive")
bufferSize = 2048
bufferExt = 16 * 3
sequenceNumber = 0
ACKData = bytearray(b'\x01\x02\x03\x04\x05')


    
with open(image %1, 'wb') as myfile:
    while True:
        if (sequenceNumber == 0):

            message, addr = serverListenSocket.recvfrom(bufferSize + bufferExt)
            message = pickle.loads(message)
            messageChecksum = packets.calculateChecksum(message[1], len(message))

            while (1):
                ACK = packets.mkepckt(ACKData, 1, packets.calculateChecksum(ACKData, len(ACKData)))
                ACKsend = pickle.dumps(ACK)
                serverSendSocket.sendto(ACKsend, (clientName, serverSendPort))
                message, addr = serverListenSocket.recvfrom(bufferSize + bufferExt)
                message = pickle.loads(message)
                messageChecksum = packets.calculateChecksum(message[1], len(message[1]))

                if(message[0] is not 0 or messageChecksum is not message[2]):
                    break
        
            packets.recvpckt(myfile, bytearray(message))
            ACK = packets.mkepckt(ACKData, 0, packets.calculateChecksum(ACKData, len(ACKData)))
            serverSendSocket.sendto(ACK, (clientName, serverSendPort))

        elif (sequenceNumber == 1):

            message, addr = serverListenSocket.recvfrom(bufferSize + bufferExt)
            message = pickle.loads(message)
            messageChecksum = packets.calculateChecksum(message[1], len(message[1]))

            while (1):
                ACK = packets.mkepckt(ACKData, 0, packets.calculateChecksum(ACKData, len(ACKData)))
                ACKsend = pickle.dumps(ACK)
                serverSendSocket.sendto(ACKsend, (clientName, serverSendPort))
                message, addr = serverListenSocket.recvfrom(bufferSize + bufferExt)
                message = pickle.loads(message)
                messageChecksum = packets.calculateChecksum(messsage[1], len(message[1]))

                if(message[0] is not 1 or messageChecksum is not message[2]):
                    break
        
            packets.recvpckt(myfile, bytearray(message))
            ACK = packets.mkepckt(ACKData, 1, packets.calculateChecksum(ACKData, len(ACKData)))
            ACKsend = pickle.dumps(ACK)
            serverSendSocket.sendto(ACKsend, (clientName, serverSendPort))
        
        
        
#file = bytearray(0)
#while(true)
 #   responseBytes = bytearray(bufferSize)
 #   (nbytes, address) = recvfrom_into(responseBytes)
  #  checksum = responseBytes[:8] // assuming 8 byte checksum
   # data = responseBytes[8:] // the rest
    #if (calculateChecksum(data, nbytes) == checksum)
    #    // Send ACK 0
    #else // Send ACK 1
   # file.append(data)

        


    
    
    