from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello World</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media1.giphy.com/media/MEdRTaYvZBlVMEjwZ3/giphy360p.mp4?cid=ecf05e47tucdy8ljyikyyzashiaom71jeye9pllitu8stukn&rid=giphy360p.mp4&ct=v", width=200>'

@app.route('/bye')
def bye():
    return "Bye"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}!, you are {number} years old"

if __name__ == "__main__":
    app.run(debug=True)
