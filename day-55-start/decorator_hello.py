# hello.py/def bye()에 몇가지 데코레이터를 추가하자
# 1. @make_bold: 글자를 볼드체로 표시 - html <b></b> 이용
# 2. @make_emphasis: 글자를 이탤릭체로 변경 - html <em></em> 이용
# 3. @make_underlined: 글자에 강조 및 밑줄 표시 - html <u></u> 이용

from flask import Flask
app = Flask(__name__)

# 1. @make_bold: 글자를 볼드체로 표시 - html <b></b> 이용
def make_bold(function):
    def bold_wrapper():
        return "<b>"+function()+"</b>"
    return bold_wrapper

# 2. @make_emphasis: 글자를 이탤릭체로 변경 - html <em></em> 이용
def make_emphasis(function):
    def emphasis_wrapper():
        return "<em>"+function()+"</em>"
    return emphasis_wrapper

# 3. @make_underlined: 글자에 강조 및 밑줄 표시 - html <u></u> 이용
def make_underlined(function):
    def underlined_wrapper():
        return "<u>"+function()+"</u>"
    return underlined_wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello World</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media1.giphy.com/media/MEdRTaYvZBlVMEjwZ3/giphy360p.mp4?cid=ecf05e47tucdy8ljyikyyzashiaom71jeye9pllitu8stukn&rid=giphy360p.mp4&ct=v", width=200>'

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}!, you are {number} years old"



if __name__ == "__main__":
    app.run(debug=True)
