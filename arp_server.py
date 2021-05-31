import socket
import subprocess
import os
localIP     = "127.0.0.1"
localPort   = 20007
bufferSize  = 1024


UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening!")


while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)

    if('Quit' in message.decode()):
    	UDPServerSocket.sendto("Disconnect".encode(), address)
    	break

    #os.system(message.decode())

    proc = subprocess.Popen('arp -a '+message.decode(), stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    print ("Output:", out.decode())
    UDPServerSocket.sendto(out,  address)

UDPServerSocket.close()