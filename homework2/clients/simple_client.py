import socket
import time
from statistics import mean

SERVER_HOST = 'localhost'
SERVER_PORT = 8090

mode = 1

client_socket = socket.socket()
client_socket.connect((SERVER_HOST, SERVER_PORT))
times = []


start = time.time()
if mode == 0:
    for i in range(1000):
        client_socket.send('Ping'.encode())
        response = client_socket.recv(100)
elif mode == 1:
    for i in range(1000):
        client_socket.send(f'{i}'.encode())
        response = client_socket.recv(100)

print(f'rps is {1000 / (time.time() - start)}')