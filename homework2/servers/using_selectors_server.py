import selectors
import socket
import time


selector = selectors.DefaultSelector()


def server():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('localhost', 8090))
    server_sock.listen()

    selector.register(
        fileobj=server_sock,
        events=selectors.EVENT_READ,
        data=accept_connection
    )


to_monitor = []

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



def accept_connection(server_sock: socket.socket) -> None:
    client_socket, client_addr = server_sock.accept()
    print(f'Connection has been received from {client_addr[0]}:{client_addr[1]}')
    selector.register(
        fileobj=client_socket,
        events=selectors.EVENT_READ,
        data=send_message
    )


def send_message(client_sock: socket.socket) -> None:
    request = client_sock.recv(4096)
    print(f'Received: {request}')
    if request:
        if request.decode() != 'Ping':
            nums = get_fib(int(request))
            client_sock.send('Fib nums were calculated'.encode())
        else:
            client_sock.send('Pong'.encode())


def event_loop():
    while True:
        events = selector.select()  # key, events (bit mask read or write)
        for key, _ in events: # key has fileobj, events, data
            callback_function = key.data
            callback_function(key.fileobj)


if __name__ == '__main__':
    server()
    event_loop()