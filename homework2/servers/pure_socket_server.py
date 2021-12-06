import socket
import time


def get_fib(n):
    fib1 = 1
    fib2 = 1
    k = 1
    while k<=n:
        sum = fib1+fib2
        fib1 = fib2
        fib2 = sum
        k+=1
    return k

def get_server_socket():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('localhost', 8090))
    server_sock.listen()

    return server_sock


server_socket = get_server_socket()

while True:
    print('Waiting new connection...')
    client_socket, client_addr = server_socket.accept()
    print(f'Connection has been received from {client_addr[0]}:{client_addr[1]}')

    while True:
        request = client_socket.recv(4096)
        print(f'Received: {request}')
        if request:
            if request.decode() != 'Ping':
                nums = get_fib(int(request))
                client_socket.send('Fib nums were calculated'.encode())
            else:
                client_socket.send('Pong'.encode())
        else:
            print('Client has gone. Closing client socket...')
            client_socket.close()
            break