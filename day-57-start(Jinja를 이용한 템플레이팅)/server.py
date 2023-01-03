from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)

current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day
current_hour = datetime.datetime.now().hour
current_min = datetime.datetime.now().minute
current_sec = datetime.datetime.now().second

@app.route('/')
def home():

    return render_template('index.html', year=current_year,
                           month=current_month, day=current_day,
                           hour=current_hour, min=current_min, sec=current_sec)

@app.route('/guess/<name>')
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]

    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html", name=name, gender=gender, age=age,
                           year=current_year,
                           month=current_month, day=current_day,
                           hour=current_hour, min=current_min, sec=current_sec)
@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)

if __name__=="__main__":
    app.run(debug=True)