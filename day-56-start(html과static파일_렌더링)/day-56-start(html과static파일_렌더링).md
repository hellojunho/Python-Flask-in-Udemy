# day 56 - html파일 & static파일 렌더링
플라스크에서는 항상 `return f"Hello{name}"`과 같이 `값`들을 리턴했다.  
다른 경우에는 리턴값에 `html/css코드`를 임의로 붙여서 리턴했었다.  
그런데 html파일을 로드할 수는 없을까?  
`렌더링`방법을 사용하면 가능하다!  

# 렌더링
`render_template`를 import하여 메소드를 활용하면 `.html`파일을 가져올 수 있다.  
먼저 프로젝트에 `template`폴더를 생성하고 그 안에 html파일을 만들자.  
나는 `my-personal-site/templates/index.html`과 같은 경로로 파일을 만들었다.  

[예시]  
```commandline
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
```
위의 코드처럼 `render_template('html파일명')`을 활용하면 html파일을 리턴할 수 있다!  