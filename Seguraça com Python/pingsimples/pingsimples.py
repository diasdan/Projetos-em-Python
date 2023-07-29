import os


def ping():

    print('''
    
    ############################################
     _______     _    ____      _      _______
    | ____  \   |_|  | |\ \    | |    / /---- \´
    | |   |  |   _   | | \ \   | |   / /     \_\´
    | |___|  |  | |  | |  \ \  | |  | |    _____
    |  _____/   | |  | |   \ \ | |  |  \  |____ |
    | |         | |  | |    \ \| |   \  \_____| |
    |_|         |_|  |_|     \___|    \________/
    
    ############################################
    ''')

    ip_ou_host = input("Digite o IP a ser verificado: ")
    qntd_pacotes = input("Quantidade de pacotes: ")
    os.system(f'ping -n {qntd_pacotes} {ip_ou_host}')
    return 0

ping()