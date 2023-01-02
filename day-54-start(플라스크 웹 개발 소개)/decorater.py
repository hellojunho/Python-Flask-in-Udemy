# Python Decorator Function

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

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")

decorated_function = delay_decorator(say_greeting)
decorated_function()