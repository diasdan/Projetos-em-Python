import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        #socket.AF_INET - uso do IP
        #socket.SOCK_STREAM - utilizaremos o TCP
        #0 - número que representa o protocolo TCP
    except socket.error as e:
        print("Conection failed.")
        print(f"Error: {e}")
        sys.exit()
        #sai da aplicação
    print("Socket created sucessfully")

    HostAlvo = input("Host or IP: ")
    PortaAlvo = input("Port: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print(f"TCP Client connected sucessfully in {HostAlvo} in port {PortaAlvo}")
        s.shutdown(2)
    except socket.error as e:
        print(f"Not possible to connect in host {HostAlvo}")
        print(f"Error: {e}")
        sys.exit()

if __name__ == "__main__":
    main()