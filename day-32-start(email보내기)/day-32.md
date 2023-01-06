# day 32 - email보내기

# 이메일은 어떻게 동작하는가?
`송신자: hellojunho@gmail.com`, `수신자: hijunho@naver.com`이 있다고 하자.  
`송신자`가 보낸 이메일은 `Gmail Mail Server` -> `Naver Mail Server` -> `수신자`의 과정을 거친다.  
이런 과정이 동작하기 위해서는 `SMTP`라는 것이 필요하다!  

# SMTP란?
`SMTP`는 `Simple Mail Transfer Protocol`의 약자로, 이메일을 메일 서버가 어떻게 받고, 다음 메일을 서버로 어떻게 전송하는 등의
 동작들이 담겨있다.  
메일 서버를 우체국으로 가정하면, 수신자는 우편함이고, SMTP는 우편함에 메시지를 넣는 방법을 알고있는 우체부

[SMTP info]

| host |Gmail|Hotmail| Yahoo               |
|------|----|----|---------------------|
| host |smtp.gmail.com|smtp.mail.yahoo.com| smtp.mail.yahoo.com |

```commandline
import smtplib

my_email = "jo62698476@gmail.com"

connection = smtplib.SMTP("smtp.gmail.com")
```  

# TLS
`TLS`란 `Transport Layer Security`의 약자로, 이메일 서버와의 연결을 안전하게 만드는 방식임!  
그럼 우리가 이메일을 전송할 때 누군가가 이메일을 가로채서 읽으려고 한다면 TLS로 인해 그 메시지가 암호화 되어 내용을 가로채서 읽을 수 없다!  


# 오류
```C:\Users\junho\PycharmProjects\Python-Flask-in-Udemy\day-32-start(email보내기)\venv\Scripts\python.exe "C:\Users\junho\PycharmProjects\Python-Flask-in-Udemy\day-32-start(email보내기)\main.py" 
Traceback (most recent call last):
  File "C:\Users\junho\PycharmProjects\Python-Flask-in-Udemy\day-32-start(email보내기)\main.py", line 8, in <module>
    connection.login(user=my_email, password=password)
  File "C:\Users\junho\AppData\Local\Programs\Python\Python311\Lib\smtplib.py", line 750, in login
    raise last_exception
  File "C:\Users\junho\AppData\Local\Programs\Python\Python311\Lib\smtplib.py", line 739, in login
    (code, resp) = self.auth(
                   ^^^^^^^^^^
  File "C:\Users\junho\AppData\Local\Programs\Python\Python311\Lib\smtplib.py", line 662, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials q11-20020a65494b000000b0047850cecbdesm790934pgs.69 - gsmtp')

Process finished with exit code 1
```
이런 오류 메시지가 발생했다?!  
강의에 나온 해결 방법을 적용해보자!  

[해결방법]  
gmail이 기본적으로 보안에 되게 빡세서 그런거라고 함..  
먼저 에러 코드에 나온 url로 들어가보자.  [https://support.google.com/mail/?p=BadCredentials](`https://support.google.com/mail/?p=BadCredentials)
1. 위 주소로 접속한 후, `내 계정/보안` 으로 들어가자.    
![image](https://user-images.githubusercontent.com/104587537/211009449-93e213b7-b06e-4902-a651-fe63a3b98de4.png)
2. `보안수준이 낮은 앱`파트가 있는데 이게 `off`로 되어있으면 `on`으로 바꿔주라고 한다.  
![image](https://user-images.githubusercontent.com/104587537/211009921-89865389-8807-4508-b41b-1e4e64afef29.png)  
그런데, ![image](https://user-images.githubusercontent.com/104587537/211010003-f2288d0d-38ca-496c-906f-b7057a7ce609.png)  
이렇다고 해서 그 다음에는 어떻게 해야되는지 모르겠다.. ㅎㅎ


[2023-01-06 : 21:33]  
main.py 어떻게 해야되는지 모르겠다..  