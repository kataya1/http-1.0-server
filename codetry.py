'''
def clientinput():
    sentence = input()
    while 1:
        msg = input()
        if msg == '':
            sentence += '\r\n'
            break
        sentence =sentence +'\r\n'+ msg
    print(sentence)

clientinput()
'''

# full_msg = ''
# while True:
#     msg = s.recv(1024)
#     if len(msg)<= 0:
#         break
#     full_msg += msg.decode()
# print(full_msg)


# sentence = connectionSocket.recv(1024).decode()
# msg = 'http/1.1'
# statuscode = 200
# statusmsg = 'ok'
# final = msg + str(statuscode) + statusmsg
# print(final.split())
msg = '/index.html\n\r'

print(msg[1:])