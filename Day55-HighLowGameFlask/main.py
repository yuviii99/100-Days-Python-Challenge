from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wrapper_function():


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == "__main__":
    app.run()
