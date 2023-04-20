import socket
import sys

ports = range(1000)
host = 'localhost'

def scanner(host, ports, timeout=0.05):
    print('\nO programa tentará ler as 1000 primeiras portas do HOST passado\n')

    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(timeout)
        try:
            code = client.connect_ex((host, port))
            if (code == 0):
                print('[+] {} porta aberta 😀'.format(port))
        except Exception as error:
            print('Não foi possível conectar-se, erro: {}'.format(error))


if __name__=='__main__':
    try:
        scanner(sys.argv[1], ports)
    except Exception as error: 
        print('\nCOMO USAR: python port-scaning.py {URL do Host}\n')