import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #objeto de conexão
#ipv4 udp

print("Socket client created sucessfully")

host = 'localhost' #qual o host
port = 5433 #qual porta receberá a conexão
message = input("Mensagem: ")

try:
    print(f'Client: {message}')
    s.sendto(message.encode(), (host, 5432)) # empacota a mensagem e envia ao servidor na porta 5432
    data, server = s.recvfrom(4096) # espera uma resposta de 4096 bytes
    data = data.decode() #quando receber a resposta, vai pegar os dados, desempacota-los e printa-los
    print(f"Client: {data}")
finally:
    print("Client: closing connection")
    s.close() #fecha a conexão para não ficar em looping

# SE CONECTA AO SERVIDOR, ENVIA A MENSAGEM E ESPERA A RESPOSTA, PARA VER SE FOI FEITO O SYNACK