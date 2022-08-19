import socketserver

class BotHandler(socketserver.BaseRequestHandler):

    def handle(self):
        "handle any request received "
        self.data=self.request.recv(1024).strip()
        print("BotName {} with IP {} sent : ".format(self.data,self.client_address[0]))
        print('sending command ...')
        self.cmdlist=[]
        with open('commands.txt') as file:
            self.cmdlist = [line.strip() for line in file if line.strip()]
            
        for i in self.cmdlist:
            print('RUN {} :'.format(i))
            self.request.sendall(i.strip().encode())
            self.data=self.request.recv(1024).strip()
            print('\toutput : {}'.format(self.data))    
        self.request.sendall('end'.encode())
        pass

if __name__=='__main__':
    HOST,PORT='',8000
    tcpserver=socketserver.TCPServer((HOST,PORT),BotHandler)
    try:
        print('Bot server is listening...')
        tcpserver.serve_forever()
    except Exception as e:
        print('Oups ! : An error occured .')
        print(e)

