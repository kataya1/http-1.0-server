from socket import *

def clientconnection():
    clientSocket = socket(AF_INET, SOCK_STREAM)
    while 1:
        try:
            keyword, serverName, serverPort = input().split()
               
            if keyword == 'connect':
                try:
                    clientSocket.connect((serverName, int(serverPort)))
                    print("Connection established...")
                    break
                except:
                    print("Connection failed try again") 
            else:
                print(f'{keyword} is an unknow command try connect')
        except ValueError as Argument:
            print(Argument)
    # serverName = '127.0.69.69' #😉
    # serverPort = 16969 
    #af_inet is ipv4

    #the program assign a client port number by default,also the client ip kinda

           
    request = clientinput()
        ## command, path, httpversion = input().split()
    clientSocket.send(request.encode())
    modifiedSentence = clientSocket.recv(1024)
    print('From Server:', modifiedSentence.decode())
    clientSocket.close()
    
def clientinput():
    sentence = input()
    while 1:
        msg = input()
        if msg == '':
            sentence += '\r\n'
            break
        sentence =sentence +'\r\n'+ msg
    return sentence

clientconnection()

