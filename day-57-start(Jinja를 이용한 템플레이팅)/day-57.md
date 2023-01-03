# day 57 - Jinja를 이용한 웹 템플레이팅

## 렌더링할 파일들은 왜 templates폴더에 있어야 할까?
내가 html파일을 렌더링 하는 것인데 왜 템플릿을 렌더링 하는걸까?  
이유는 내가 `템플레이팅 언어`로 작업하는 방법을 알고 있는 한 html파일도 템플릿과
 똑같은 역할을 하기 때문이다.  

## Jinja
`Jinja`는 템플레이팅 언어 중 하나로, 파이썬에서만 가능하다.  
html파일 내부에서 실제로 파이썬 코드로 평가하는 부분을 지정하기 위해 `{{}}`와 같은 코드를 사용함.  

[예시]  
`index.html`에서 h1태그 부분에 5 * 6을 입력하고 실행하면 브라우저에는 달랑 "5 * 6"만 나올 것이다.   
```commandline
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My WebSite</title>
</head>
<body>
    <h1>5 * 6</h1>
</body>
</html>
```  
그런데 `Jinja`문법인 `{{}}`를 사용해 `5 * 6 -> {{5 * 6}}`으로 표현한다면?  
그러면 프로그램에서 `{{5 * 6}}`를 파이썬 코드로 판단하게 된다.  
```commandline
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My WebSite</title>
</head>
<body>
    <h1>{{5 * 6}}</h1>
</body>
</html>
```  
위 코드를 실행하면 5 * 6이 아니라 5 * 6의 결과인 "30"이 출력된다.  

## 난수 생성하기
`index.html`에서 `Random_number: {{  }}`를 작성해보자.  
그 후에 `server.py`에서 `random_number = ramdom.randint(1, 10)`을 선언하고, 
`render_template('index.html', num=random_number)`를 리턴하면 끝!  
`render_template()` 설명서를 확인하자.  
*한 번 실행하고 새로고침 하니까 난수가 똑같은 값이 나온다? -> `shift+새로고침` 고고*  

[index.html]  
```commandline
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My WebSite</title>
</head>
<body>
    <h1>Hello World</h1>
    <h2>{{5*6}}</h2>
    <h3>Random_Number: {{ num }}</h3>
</body>
</html>
```  

[server.py]  
```commandline
from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    return render_template('index.html', num=random_number)

if __name__=="__main__":
    app.run(debug=True)
```  

[server.py]
```
@app.route('/')
def home():
    random_number = random.randint(1, 10)
    random_number2 = random.randint(1, 100)
    return render_template('index.html', num=random_number, num2=random_number2)
```  
이렇게도 가능하다!  

## 날짜 출력하기?
`server.py`에서 `import datetime`후, 연도를 원하면 `year = datetime.datetime.now().year`과 같은 형식으로 작성하면 된다.  
물론 `index.html`에서는 `Jinja`문법으로 표시해야됨!!  

나는 화면 하단에 `footer`태그를 사용하여 시간을 나타냈음!  
```commandline
<footer>
    <p> [CopyRight]<br>{{ year}}-{{month}}:{{day}}_{{hour}}:{{min}}:{{sec}}<br>Built by hellojunho</p>
</footer>
```

## API를 렌더링해보자!
이 강의에서는 [agify](https://agify.io/)와 [genderize](https://genderize.io/)라는 간단한 API를 활용했다.  
API사용을 위한 인증 같은 절차가 없어 간단하다고 한다.  

[agify]  
처음 들어가면 아래와 같은 화면이 나오는데, 드래그된 url 옆의 "TRY ME"클릭!  
![image](https://user-images.githubusercontent.com/104587537/210325271-af690809-3431-406b-abfc-d67cb5669771.png)  
그러면 간단한 json형태의 데이터가 나온다.  
![image](https://user-images.githubusercontent.com/104587537/210325405-5c1c0971-a4ea-4a5f-9853-b702bac7706c.png)  

`genderize` api도 위와 동일하게 하면 됨!

이번에 나는 이 데이터를 동적 플라스크 응용 프로그램으로 바꾸고자 한다.  
동작 예시로는 "메인URL/guess/Name"을 입력하면 화면에 Name과 성별, 나이를 예측하는 프로그램을 만드는 것이다.  
API를 가져와 쓰는 것이므로, 가장 이상적으로는 이름의 첫 글자가 대문자여야 한다.  

[server.py]  
```commandline
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

if __name__=="__main__":
    app.run(debug=True)
```  
[guess.html]  
```commandline
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My WebSite</title>
</head>
<body>
    <h1>Hello {{name.title()}}</h1>
    <h2>I think you are {{gender}}, </h2>
    <h3>And maybe {{age}} years old.</h3>
</body>
<footer>
    <p> [CopyRight]<br>{{ year}}-{{month}}:{{day}}_{{hour}}:{{min}}:{{sec}}<br>Built by hellojunho</p>
</footer>
</html>
```


## Jinja 멀티라인 구현
기존에는 `{{   }}`문법을 이용하여 한 문장만 취급했었다.  
이번에는 간단한 블로그를 만들어 볼 예정인데, [npoint](https://www.npoint.io/)를 참조하였다.  
![image](https://user-images.githubusercontent.com/104587537/210329414-f98b3900-bb2c-428b-920a-f6e95240dff3.png)  
시작화면에서 시작하기 버튼만 클릭하면 나만의 json데이터를 만들 수 있다.  
API를 만들고 나면 하단의 url로 접속하여 json데이터를 확인할 수 있다.  
![image](https://user-images.githubusercontent.com/104587537/210329588-0d6ed220-eecb-4907-9bbc-690175c56b99.png)  

[blog.html]  
```commandline
<body>
    {% for blog_post in posts: %}
        <h1>Title: {{ blog_post["title"] }} </h1>
        <h3>SubTitle: {{ blog_post["subtitle"] }}</h3>
        <br>
    {% endfor %}
</body>
```  
[server.py]  
```commandline
@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)

```  

`{%  %}`문법을 사용하면 여러 줄의 문장을 파이썬 코드로 취급할 수 있다.  
다른 예시로는   
```commandline
{% if name%}
    <h1>Hello {{ name }} </h1>
{% else %}
    <h1>Hello World</h1>
{% endif %}
```
이렇게도 사용한다.  
여기서 중요한 점은 항상 반복/조건문이 끝날 때마다 `end`를 확인시킨다는 점이다.  
`for문`의 경우에는 `{% endfor %}`, `if문`의 경우에는 `{% endif %}`처럼!!  
*약간 jsp가 생각나는 문법이다...*

## 동적으로 블로그 들어가는 법
`index.html`에 body부분에 아래와 같은 코드를 추가했다.  
[index.html]  
```commandline
<a href="{{ url_for('get_blog') }}">Go To Blog</a>
```  
모든 Jinja템플릿에서 `url_for()`이라는 메소드에 엑세스 할 수 있다고 한다.  
`url_for()`이 어디에 있을까?  
`Flask`에 내장되어 있다고 한다!  
`url_for('메소드이름')`요렇게 설정하고, `href=""`로 감싸주면 하이퍼링크 완성!  