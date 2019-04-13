from socket import *
def serverConnection(port, hostform):
    serverPort = port 
    host = hostform
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # i think it binds to a local network by default #confirmed
    # serverSocket.bind(('', serverPort))
    serverSocket.bind((host, serverPort))
    serverSocket.listen(10)
    print('The server is ready to receive')
    while True:
        # connection socket has 2 other parameters, client 
        # ip and port if the client ip is different but same port it makes a new socket
        connectionSocket, addr = serverSocket.accept()
        print(addr)
        
        sentence = ''
        while True:
            msg = connectionSocket.recv(1024)
            if len(msg)<= 0:
                break
            sentence += msg.decode()
    
        splitedByLine = sentence.split('\r\n')

        command, path, httpVersion = splitedByLine[0].split()

        if command == 'GET':
            if path == '/':
                path = 'index.html'
            if path[0] == '/':
                path = path[1:]
            try:
                f = open(path,'rb')
                reader = f.read(1024)
                statusline = httpVersion + '200 OK' + '\r\n'
                connectionSocket.send(statusline.encode())

                while reader:
                    connectionSocket.send(reader)
                    reader = f.read(1024)

            except:
                statusline = httpVersion + '404 file not found' + '\r\n'
                connectionSocket.send(statusline.encode())
                # 404 file not found
                
            
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

serverConnection(8084, 'localhost')