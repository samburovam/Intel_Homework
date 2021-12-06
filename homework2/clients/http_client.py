import requests
import time
mode = 1
url = 'http://127.0.0.1:5000/post'


def echo():
    start = time.time()
    for i in range(1000):
        post = requests.post(url, {'mode': 0, 'i': None})
    stop = time.time()
    print(f'requests per second is {1000 / (stop - start)}')

def fib():
    start = time.time()
    for i in range(1000):
        post = requests.post(url, {'mode': 1, 'i': i})
    stop = time.time()
    print(f'requests per second is {1000 / (stop - start)}')

if __name__ == '__main__':
    if mode == 0:
        echo()
    elif mode == 1:
        fib()