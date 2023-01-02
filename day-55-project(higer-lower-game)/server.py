from flask import Flask
import random

app = Flask(__name__)
num = random.randint(0, 10)
print(num)


@app.route('/')
def main():
    return '<h3 "style=text-align: center">안녕하세요! Higher-Lower 게임에 오신걸 환영합니다!</h3>' \
           '<img src="https://giphy.com/gifs/animation-retro-pixel-3o7aCSPqXE5C6T8tBC?utm_source=media-link&utm_medium=landing&utm_campaign=Media%20Links&utm_term=", width=200>'


@app.route('/<int:guess>')
def guess_number(guess):
    if guess > num:
        return "<h3 style='color: blue'>정답보다 큰 숫자를 입력했습니다!</h3>"
    elif guess < num:
        return "<h3 style='color: red'>정답보다 작은 숫자를 입력했습니다!</h3>"
    elif guess == num:
        return "<h3 style='color: green'>정답입니다!</h3>"


if __name__ == "__main__":
    app.run(debug=True)
