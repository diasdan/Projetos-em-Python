import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #objeto socket

print("Socket created sucessfully")

host = 'localhost'
port = 5432

s.bind((host, port))
#faz a ligação entre cliente e servidor através do host e da porta

while 1: #enquanto o bind for true
    data, end = s.recvfrom(4096) #recebe 4096 bytes e armazena em dados e endereço
    print(f"Cliente enviou a mensagem {data}")
    message = input("Resposta: ")

    if data:
        print('Server sending message')
        s.sendto(data + (message.encode()), end) # enpacota e envia a resposta
