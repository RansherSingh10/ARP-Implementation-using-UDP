import socket
serverAddressPort   = ("127.0.0.1", 20007)
bufferSize          = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


while (True):
    msgFromClient = input("Enter the command:")
    bytesToSend = str.encode(msgFromClient)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
   
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Server: {}".format(msgFromServer[0].decode())
    #print(msg)

    if('Quit' in msg):
    	break
    
    print("Server Output: ")
    f=open('output.txt','r')
    print(f.read())

UDPClientSocket.close()
