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

## 정적 파일 렌더링
위에 템플릿들이 `templates`폴더에 들어가있어야 하는 것처럼, 
플라스크에서는 이미지나 css파일과 같은 정적 파일들을 `static`이라는 폴더 안에서 찾는다.  
즉, `static`폴더를 생성해야 한다!  

나는 `my-personal-site/static`폴더를 만들었고, 그 안에 `hellojunho's profie_1.jpg`파일을 저장했다.  
이 정적 이미지 파일을 렌더링 하려면 html파일에서 `img src="static/hellojunho's profile_1.jpg"`와 같이 지정해줘야 한다.  
파일의 위치 표시를 위해 `statlc/`과 확장자`.jpg`잊지 말기!  

## Challenge
`index.html`에서 "home()"메소드가 실행되었을 때의 배경 색을 바꿔보자!  
css파일을 만들어야 하고, index.html에는 어떻게 설정을 해야 바뀔까?  

[static/styles.css]  
```commandline
/*index.html의 배경 색을 바꾸는 css파일*/
body {
    background-color: red /*purple, blue, ...*/
}
```

[index.html]  
`index.html`에서는 `<head></head>` 부분에 ` <link rel="stylesheet" href="static/styles.css">`을 추가해줘야 한다!  
```commandline
<head>
    <meta charset="UTF-8">
    <title>hellojunho</title>
    <link rel="stylesheet" href="static/styles.css">
</head>
```

[server.py]  
`server.py`는 이렇게!
```commandline
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
```

*소스코드를 수정하고 크롬으로 실행했는데 수정한 내용으로 안바뀌어있다? 그건 크롬에서 소스코드를 캐시하기 때문이라고 함. 이럴 때는
 `shift+새로고침`을 클릭해보자! 이건 `강력 새로고침`이라고 하더라!* 