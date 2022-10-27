import random
import struct

def mkepckt(myfile, sequenceNumber, checksum):
    
    bits = (sequenceNumber, myfile, checksum)
    return bits


def recvpckt(myfile, data):

    myfile.write(data)
    myfile.flush()

#def checksum(bufferSize, myfile):
 #   checksumVal[0]
  #  string = open(myfile, 'rb')
   # listThing = list(myfile)
    #for i in range(0,buffer):
     #   data = string.read(i*2) or listThing[i] + listThing[i+1]
      #  checksumVal[0] += data
   # checksumVal = ~checksumVal
   # string.close

    #return checksumVal[0]


def calculateChecksum(data, nbytes):
    sum = 0
    for ch in data:
        sum += ch
   # for i in range(0, nbytes)[0::2]:
    #    (word16, timestamp) = struct.unpack('>I', data[i:2])
     #   sum += word16
    #if (size & 1 == 1):
     #   (word16, timestamp) = struct.unpack('>I', data[nbytes-1])
      #  sum += word16
   # while (s >> 16 > 0):
    #    sum = (sum & 0xFFFF) + (sum >> 16)
    return ~sum

def pcktscrmblr(percentage, bufferSize, myfile, *totalbits):
    count = 0
    tempOpen = open(myfile, 'rb')
    for i in range(0, bufferSize):
        temp = tempOpen.read(1)
        test = random.random()
        if (test < percentage and count/totalbits < percentage):
            temp = ~temp
            count += count
        data += temp

    totalbits += bufferSize
    return data
