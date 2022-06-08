import re
from flask import Flask
app = Flask(__name__)


def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    last_value = 1
    current_value = 1
    for i in range(n-1):
        aux_value = current_value
        current_value += last_value
        last_value = aux_value

    return current_value


@app.route('/fibonacci/<int:x>')
def res(x):
    respuesta = fibonacci(x)
    return f"{respuesta}"


@app.route('/')
def index():
    return "Hello word"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
