# day 61 - 고급 입력 양식 만들기
플라스크 확장 모듈인 `Flask-WTF`를 사용하여 입력양식을 만든다.  

## 61.1 Flask-WTF 설치

[https://wtforms.readthedocs.io/en/2.3.x/](https://wtforms.readthedocs.io/en/2.3.x/)  
터미널: pip install Flask-WTF  
*pip install은 대소문자를 구분한다!*  



[장점]  
- 쉬운 유효성 검증
  - 사용자가 필수 입력 항목에 올바른 형식으로 데이터를 입력했는지 검증
    - 예) 사용자가 입력한 이메일 주소에 '@', '.'등의 포함 여부 확인
- 코드 라인 감소
  - 웹사이트에 입력양식을 많이 사용한다면, 플라스크 입력양식 모듈을 사용하면 작성해야하는 코드의 양을 획기적으로 줄일 수 있음
- CSRF 보호 기능 내장
  - `사이트 간 요청 위조(CSRF)`는 모르는 사람에게 돈을 송금하는 등의 사용자가 자신의 의지와는 무관한 행동을 하게 하는 공격
  - 이런 공격으로부터 보호해주는 기능이 내장되어 있음


## 61.2 Flask-WTF로 입력양식 만들기
[https://flask-wtf.readthedocs.io/en/1.0.x/form/](https://flask-wtf.readthedocs.io/en/1.0.x/form/) < 여기에 접속해서 읽어보고, 
간단한 로그인 양식을 만들어보자.  

- email, password 항목은 반드시 있어야 함
- 이 항목들은 StringFields로 만들면 됨
- validators에 대해 신경 쓰지 않아도 됨
- email과 password 입력창은 크기(너비)가 30이어야 합니다.
- HTML로 <label>이나 <input> 요소를 직접 만들어서는 안 됩니다.

힌트: CSRF 보호 기능을 넣고 싶다면, login.html에 아래 코드를 추가해야 합니다.  
```angular2html
{ form.csrf_token }} 
```  
또, main.py에서 csrf_token을 생성하는 데 사용될 [비밀키](https://stackoverflow.com/questions/22463939/demystify-flask-app-secret-key)를 만들어야 합니다.  
```angular2html
app.secret_key = "some secret string"
```  

[해답]  
[https://gist.github.com/angelabauer/162f56578b9193090963a0691c826790](https://gist.github.com/angelabauer/162f56578b9193090963a0691c826790)  

