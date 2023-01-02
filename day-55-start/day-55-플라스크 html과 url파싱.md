# day-55-플라스크 html과 url파싱법

# 라우팅(Routing)
플라스크에서의 라우팅이란 `@app.route()`로 동작하며, `@app.route('/')`과 같이 
'`/`'이 붙었으면 메인 url뒤에 /를 붙여 페이지로 들어간다는 의미이다.  

[예시]  
```commandline
@app.route('hello')
def hello():
    return "Hello World"
```  
코드가 위와 같고, 메인 url이 "www.hello.com"이라고 하면, "`www.hello.com/hello`" 처럼 사용하면 
페이지에 "`Hello World`"가 나오게 된다.  


## app.route에 변수할당
만약 사용자의 이름마다 다르게 Hello Junho 혹은 Hello Minji 뜨게 하는 방법은 없을까?  
`app.route('/username/<username>')`과 같은 형식으로 지정하면 된다!  
  
[예시]  
```commandline
@app.route("/username/<name>")
def greet(name):
    return f"Hello{name}"
```   
위의 코드를 입력하고 실행시켜보자.  
`http://127.0.0.1:5000`의 url을 부여받고, `http://127.0.0.1:5000/username/Junho`를 입력하면, 
화면에 "Hello Junho"가 출력되는 것을 확인할 수 있다.  

## 디버그 모드
서버가 켜져있는 상태에서 내가 코드를 수정하고 다시 화면을 띄워본다면, 내가 수정한 대로 동작하지 않을 것이다.  
그 이유는 바로 서버가 켜져있기 때문에 다시 부팅을 해주어야 수정 내용이 반영되기 때문이다.  
너무 귀찮다.  하지만 이럴 때 유용하게 사용할 수 있는 기능이 `디버그 모드`이다!  

[디버그 모드의 장점]  
1. 이 기능을 통해 디버거를 활성화 할 수 있다.
2. 어떤 이슈가 발생했는지 추려갈 수 있다.  

### 그래서 어떻게 사용할까?
디버그 속성을 `True`로 바꿔주기만 하면 끝!  
그리고 다시 서버를 재시작하자!  

[예시]  
```commandline
if __name__ == "__main__":
    app.run(debug=True)
```

서버를 재실행 했을 때 실행 콘솔 창에 `Debug mode: on`이라고 나와야 정상임.  
이 상태에서 서버를 끄지 않고 코드를 수정해보자!  
나는 "return f"Hello there {name}!""으로 수정하고 서버를 부팅하지 않고 브라우저에서 새로고침을 했다.  
결과는 수정한 내용이 정상 반영되었다!  
`Detected change in 'C:~~~''`와 같은 알림 메시지가 뜨면 디버거가 수정을 감지하고 반영하여 알아서 서버를 재시작해준다는 의미였다.  

## return값에 html/css적용
함수의 리턴값에 html/css 태그를 적용시켜 사용할 수 있다.
[예시]  
```commandline
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello World</h1>'
```  
위의 코드는 return 값에 `html: <h1></h1>`, `css: style="text-align: center`를 적용시켰다.  
실행 시키면 "Hello World"가 메인화면 가운데에 출력된다.  

return값에 html 태그를 하나만 사용할 수 있을까?
아니다.  
> return '<h1 style="text-align: center">Hello World</h1><p>This is a paragraph</p>
  
이 코드처럼 h1태그 뒤에 p태그가 붙은 것처럼 이어 사용할 수 있다.  

한 줄에 코드가 너무 길게 들어간다면?  
그냥 `엔터`누르자!  
그럼 자동으로 줄이 분리된다.  

[예시]  
```commandline
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello World</h1>' \
           '<p>This is a paragraph</p>'
```  
