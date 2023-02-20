import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8888))

server.listen()
client, end = server.accept()

closed = False

while not closed:
    msg = client.recv(1024).decode('utf-8')
    if msg == 'tt':
        closed = True
    else:
        print(msg)
    client.send(input('Mensagem: ').encode('utf-8'))

client.close()
server.close()
