from flask import Flask
import random

app = Flask(__name__)

print(random.__name__)  # 모듈명: random이 출력됨
print(__name__)         # __main__이 출력됨

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/bye")
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()