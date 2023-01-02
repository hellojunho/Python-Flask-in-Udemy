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

## 플라스크 서버
플라스크를 사용하여 동작하는 서버는 개발용 서버이므로 상품화하여 배포 금지!  
*WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.*  

## 일급 객체
파이썬 함수는 `일급 객체`로 알려져있다.  
즉, 함수를 인자로 전달할 수 있다는 뜻이다!  
매개변수를 넘겨줄 떄와 똑같이 취급하면 됨  

[예시]  
```commandline
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# First-class objects, can be passed around as arguments e.g. int/string/float etc.
def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)

result = calculate(multiply, 2, 3)
print(result)
```
원래대로라면 2 * 3 = 6이 출력됨.
이유는 함수가 `일급 객체`로 취급되기 때문에 함수를 숫자, 문자열처럼 다른 함수에 전달할 수 있기 때문

## Nested Function (함수 안의 함수)
`Nested Function`은 함수 안에서 선언한 함수이다.  
`내부 함수`라고 기억해야겠다.  

[예시]  
```commandline
# Nested Functions (함수 안에 함수 선언)
def outer_function():
    print("I'm outer")
    
    def nested_function():
        print("I'm inner")
    
    return nested_function
```
nested_function()은 outer_function()안의 영역에서만 호출이 가능하다.  
즉, outer_function()밖에서 nested_function()을 입력해도 호출 안됨!  
별 다른 조건이 없으면 outer_function()을 실행하면 nested_function()도 실행됨.  

outer_function()의 return값이 nested_function인 것과 같이 함수를 return할 수도 있다.  


## 파이썬 데코레이터
`데코레이터 함수`란 플라스크에서 `@app.route()`같은 함수처럼 `@`를 앞에 붙여 사용하는 함수를 말한다.  
`decorate.py`에서 delay_decorator는 안에 wrapper_function을 감싸고, 그 안에서 function이라는 기능이 2번 실행된다.  
데코레이터 함수는 wrapper_function을 감싸고 있는 것처럼 함수를 감싸고 있으며, 추가적인 기능을 실행시키는 함수를 뜻한다.  

[예시]  
```commandline
import time

# 데코레이터 함수란, 단순히 다른 함수를 감싸 추가 기능을 부여하는 함수
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something after
    return wrapper_function
# 이제 어떤 함수든 delay_decorator 실행하면 2초 늦게 실행됨

@delay_decorator # 시간 지연을 줄 메소드 앞에 붙여줌
def say_hello():
    print("Hello")

say_hello()
```  
위의 코드에서 보이는 것과 같이 `@delay_decorator`이 붙은 함수 `say_hello`는 데코레이터 함수로 전달되어 동작한다.  
출력 결과는 `time.sleep(2)`를 `delay_decorator`에서 사용했지만 2초 뒤에 "Hello"가 출력되는 것을 볼 수 있다.  