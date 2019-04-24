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
                print(f"{keyword} is an unknow command try connect")
        except ValueError as Argument:
            print(Argument)
    # serverName = '127.0.69.69' #😉
    # serverPort = 16969 
    #af_inet is ipv4

    #the program assign a client port number by default,also the client ip kinda

           
    request, path, command = clientinput()
    if command == 'GET':
        clientSocket.send(request.encode())
    if command == 'POST':
        file = open(pathFixer(path),'r')
        data = file.read()
        request+= data
        clientSocket.send(request.encode())

        

    sentence = ''   

    while True:
        msg = clientSocket.recv(1024)
        try:
            sentence += msg.decode()
        except:
            sentence += msg.decode("bin64")
        # print(msg)
        if ((sentence[-4:] == '\r\n\r\n')or(len(msg)<= 0)):
            break
    fileModify(sentence, path, command)
    # modifiedSentence = clientSocket.recv(1024)
    # print('From Server:', modifiedSentence.decode())

    clientSocket.close()
    
def clientinput():
    sentence = input()
    command, path, httpversion = sentence.split()
    
    while 1:
        msg = input()
        if msg == '':
            # print("broke out")
            sentence += '\r\n\r\n'
            break
        sentence =sentence +'\r\n'+ msg
    return sentence ,path, command

def pathFixer(path):
    if path == '/':
        fixedp = 'index.html'
    elif path[0] == '/':
        fixedp = path[1:]
    return fixedp

def fileModify(msg, path, command):
    #message separated by lines
    msgSep = msg.split('\r\n')
    print(msgSep[0])
    try:
        httpversion, statuscode, statusDescriptor = msgSep[0].split()
    except:
        statuscode = '0'
        print("bad recieve")

    if statuscode == '200' and command == 'GET':
        truepath = pathFixer(path)
        writer = open(truepath,'w')
        print(msg[len(msgSep[0]):])
        writer.write(msg[len(msgSep[0]):])
    elif statuscode == '200' and command == 'POST':
        print("file reached there safely")
    elif statuscode == '404':
        print('file is not there buddy')
    else:
        print("??????")
    
    
clientconnection()

