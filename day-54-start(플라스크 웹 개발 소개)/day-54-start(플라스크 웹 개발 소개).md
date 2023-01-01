# day 54 - 플라스크 웹 개발 소개

# 파이썬 웹 프레임워크
대표적인 파이썬 웹 프레임워크는 `플라스크(Flask)`, `장고(Django)`가 있다.  
`플라스크`는 초보자와 소규모 프로젝트에 적합하고, `장고`는 대규모 사업 프로젝트에 적합하다고 한다.  


# 프레임워크와 라이브러리
`BeautifulSoup`과 같은 `라이브러리`는 특정 기능이 필요할 때 언제든 접근해 활용할 수 있는 툴이다.  
`프레임워크`는 라이브러리와 비슷하지만 직접 작성하지 않은 코드의 묶음이다.  
둘의 가장 큰 차이는 `라이브러리`는 사용하려는 메소드를 라이브러리로부터 호출해야 하지만, 
`프레임워크`는 프레임워크의 규칙에 맞게 아키텍처를 사용하고 특정 기능을 실행할 때 프레임워크가 내가 작성한 코드를 호출한다는 점이다.  
무슨 말일까?  
request 라이브러리를 사용했을 때 request.get()을 쓰고 안에 호출하려는 url을 넣어 주소를 불러온다.  
하지만 프레임워크는 내가 프레임워크에 맞게 코드를 작성해야 프레임워크에서 내가 만든 메소드를 호출한다. (내가 프레임워크를 호출하는 것이 아니라.)  

# 플라스크 실행하기
[플라스크 공식 홈페이지에서 Quickstart](https://flask.palletsprojects.com/en/2.2.x/quickstart/)를 클릭해 들어가면 
기본 실행 코드를 볼 수 있다.  
[hello.py]  
```commandline
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
```
위 코드를 실행했을 때 나는 자꾸 아래와 같은 에러코드가 발생했다.  
> error: failed to find flask application or factory in module 'app'. use 'app:name' to sp ecify one.  

`hello.py`의 맨 아래에 아래의 코드를 추가하였더니 해결되었다.
[추가할 코드]  
```commandline
if __name__ == '__main__':
    app.run()
```

[결과적으로 이 코드]  
```commandline
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
    
if __name__ == '__main__':
    app.run()
```

[코드 실행 방법]  
1. 터미널에서 실행 방법 (윈도우)
> \> set FLASK_APP=hello.py
> \> flask run

2. 터미널에서 실행 방법 (맥)
> \> export FLASK_APP=hello.py
> \> flask run

3. 단축키 실행 방법
> ctrl + shift + f10

## __name__
`__name__`은 뭘까?  
아래 코드를 실행해보자.  
[__name__ 출력 코드]
```commandline
from flask import Flask

app = Flask(__name__)

print(__name__)
```
`__main__`이 출력될 것이다.  
`__name__`은 파이썬에 내장된 특수 속성 중의 하나이다. 언제라도 __name__에 접근하면 
현재 사용중인 함수, 메소드, 디스크립터의 이름을 알 수 있다.  
출력이 `__main__`이라는 것은 코드가 특정 모듈에서 실행 중이라는 뜻이다.  

```commandline
if __name__=="__main__":
    # execute only if run as a script
    main()
```
위 코드는 `__name__==__main__`가 참이면 스크립트로 실행될 때만 main()을 실행.  
내가 아까 위에서 `hello.py`에 추가한 코드랑 똑같음!  