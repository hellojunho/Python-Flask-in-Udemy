# day 17

## 클래스
클래스란 한 객체를 생성하고 그 객체에 속성(메소드)들을 부여해 객체마다 다른 메소드들을 호출하여 사용할 수 있도록 함.

### 클래스 생성하기
```commandline
class 클래스명:
    ~~~
```
이와 같은 형식으로 클래스를 생성할 수 있다.  

### 생성자
생성자는 객체의 속성들을 초기화 해준다.  
*하지만 객체를 선언할 때 항상 모든 속성들이 초기화 될 필요는 없음*
    예) 인스타그램의 경우에 만약 팔로워 수를 항상 초기화 한다고 하면 프로그램을 실행할 때 마다 팔로워 수가 0이 될 것이다.  

[예시]
```commandline
class User:
    __init__(self, user_id, username):
        self.id = user_id
        self.username= username
```
생성자를 만들면 객체를 선언할 때, 객체의 값들을 지정하여 선언할 수 있다.  
파이썬에서는 생성자에서 각 값들을 초기화 할 때, 기본값을 주어 초기화 할 수도 있다. 
    > 예) self.followers = 0
[기존]
```commandline
user1 = User()
user1.id = "001"
user1.username = "hello"
```

[생성자 적용 후]
```commandline
user1 = User("001", "hello")
```

### self
클래스 내부에서 정의된 메소드의 경우에는 항상 첫 번째 인자는 `self`이다.  
이유가 뭘까?  
대부분의 경우에는 첫 번째로 `self`매개변수가 오는 경우가 많지만, 항상 그런 것은 아니다.  

```commandline
class Foo:
    def func1():
        print("function 1")
    def func2(self):
        print("function 2")    
```
위와 같은 클래스가 있다고 하자. 
```commandline
\>>> f = Foo()
\>>> f.func2()
function2
```
위의 경우처럼 사용하면, self에 대한 값은 파이썬이 자동으로 넘겨주기 때문에 아무 이상 없이 실행된다.  

```commandline

\>>> f.func1()
Traceback (most recent call last):
    File "<pyshell#25>", line 1, in <module>
        f.func1()
TypeError: func1() takes 0 position arguments but 1 was given
```
위의 경우는 "func1()은 인자가 없지만 1개의 인자를 받았다."라는 의미로, self가 없는 함수 func1()를 호출할 경우에 생기는 오류이다.  

```commandline
\>>> class Foo:
        def func1():
                print("function 1")

        def func2(self):
                print(id(self))
                print("function 2")
                
>>> f = Foo()
>>> id(f)
43219856

>>> f.func2()
43219856
function 2     
```
위의 경우처럼 객체의 아이디 출력과, func2()에서 self값을 넘겨주어 id를 출력했을 때의 값이 같은 것을 알 수 있다.  
![image](https://user-images.githubusercontent.com/104587537/210162783-842cad5e-8757-4bc7-9ff9-b4fabe826dea.png)  
결과적으로, 클래스 내에 정의된 self는 `클래스 인스턴스`임을 알 수 있다.  
그게 뭐냐? 결국 `객체 자기 자신을 참조하는 매개변수`이다.  

### 