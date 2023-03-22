import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket Criado com Sucesso')

host = 'localhost'
port = 5432

s.bind((host, port))
mensagem = '\nServidor: Olá, cliente'

while 1:
    dados, end = s.recvfrom(4096)

if dados:
    print('\nServidor enviando mensagem...')
    s.sendto(dados + (mensagem.encode()), end)

