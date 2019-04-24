from socket import *
def serverConnection(port, hostform):
    serverPort = port 
    host = hostform
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # i think it binds to a local network by default #confirmed
    # serverSocket.bind(('', serverPort))
    serverSocket.bind((host, serverPort))
    serverSocket.listen(20)
    print('The server is ready to receive')
    while True:
        # connection socket has 2 other parameters, client 
        # ip and port if the client ip is different but same port it makes a new socket
        connectionSocket, addr = serverSocket.accept()
        print(addr)
        
        sentence = ''
        while True:
            msg = connectionSocket.recv(1024)
            sentence += msg.decode()
            print(msg)
            if ((sentence[-4:] == '\r\n\r\n')or(len(msg)<= 0)):#sentence[-4:] == '\r\n\r\n') or 
                print('broke out')
                break
            # sentence += msg.decode()
        print('THIS IS THE MESSAGE BIIISH ' + sentence)
        print(sentence)
        splitedByLine = sentence.split('\r\n')
        
        command, path, httpVersion = splitedByLine[0].split()
        print(command,path,httpVersion)
        if command == 'GET':
            # if path == '/':
            #     path = 'index.html'
            # if path[0] == '/':
            #     path = path[1:]
            truePath = pathFixer(path)
            print(path , 'fixed the path' , truePath)
            try:
                f = open(truePath,'rb')
                print("opened the file")
                reader = f.read(1024)
                statusline = httpVersion + ' 200 OK' + '\r\n'
                connectionSocket.send(statusline.encode())

                while reader:
                    print("sending....")
                    connectionSocket.send(reader)
                    reader = f.read(1024)

            except FileNotFoundError:
                statusline = httpVersion + ' 404 file_not_found' + '\r\n'
                connectionSocket.send(statusline.encode())
                # 404 file not found
        elif command == 'POST':
            fileModify(sentence, path, command)
        else:
            statusline = httpVersion + ' 400 BAD_REQUEST' + '\r\n'
            print("...what!!?")
                
            
        # connectionSocket.send(capitalizedSentence.encode())
        connectionSocket.close()
        print("Connection to addr has been terminated")

def commandHandler(command,path):
    if command == 'GET':
        pass
    elif command == 'POST':
        pass
    else:
        pass
# serverSocket.detach()

# def messageReciever()
def pathFixer(path):
    
    if path == '/':
        fixedp = 'index.html'
    elif path[0] == '/':
        fixedp = path[1:]
    return fixedp

def fileModify(msg, path, command):
    #message separated by lines
    msgSepHEADDATA = msg.split('\r\n\r\n')
    msgSep = msgSepHEADDATA[0].split('\r\n')
    print("heeeeeeeeeeeeey loook here" + msgSep[0])
    try:
        httpversion, statuscode, statusDescriptor = msgSep[0].split()
    except:
        statuscode = '0'
        print("bad recieve")

    if statuscode == '200' and command == 'GET':
        pass
    elif statuscode == '200' and command == 'POST':
        truepath = pathFixer(path)
        writer = open(truepath,'w')
        print(msg[len(msgSep[0]):])
        writer.write(msg[len(msgSep[0]):])
    elif statuscode == '404':
        print('file is not there buddy')
    else:
        print("??????")

serverConnection(8086, 'localhost')
