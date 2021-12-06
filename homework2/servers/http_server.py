from flask import Flask, json, request
import time

cities = [
    {'id': 1, 'name': 'Archangelsk'},
    {'id': 2, 'name': 'Moscow'},
    {'id': 3, 'name': 'Nizhniy Novgorod'}
]
mode = 0
app = Flask(__name__)

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

@app.route('/cities', methods=['GET'])
def get_cities():
    return json.dumps(cities, indent=4)


@app.route("/")
def main_page():
    return "<p>Welcome to Flask!</p>"

@app.route("/post", methods=["POST"])
def post_request():
    if request.json['mode'] == 0:
        return 'Ping'
    elif request.json['mode'] == 1:
        nums = get_fib(request.json['i'])
        print(nums)
        return str(nums)

if __name__ == '__main__':
    app.run()