# day 60 - project2

# 과제 1
아래 문서를 참고하여, HTML 입력양식에 입력된 데이터를 "POST" 요청 방식으로 
 "/login" 경로에 전달하는 방법을 알아보세요.

[https://www.w3schools.com/tags/att_form_method.asp](https://www.w3schools.com/tags/att_form_method.asp)

[해답](https://gist.github.com/angelabauer/889ac7cfdfed5cfeb79559f41c9c6a07)


# 과제 2
 입력양식을 제출했으면, 서버에서 이 POST 요청을 받아야 합니다. 그러려면 먼저 입력양식의 각 입력 값에 name 속성이 있어야 해요.
![image](https://user-images.githubusercontent.com/104587537/210976817-a927f100-bf82-4bde-957d-93df676e46a4.png)
 


# 과제 3
이제 POST 요청을 받았을 때, 이 요청을 처리하도록 데코레이터를 main.py 안에 만들면 됩니다.
![image](https://user-images.githubusercontent.com/104587537/210976858-cea44582-6445-436a-b572-c5cda8be22ba.png)
methods 매개변수는 딕셔너리 형으로 쓸 수 있으므로 하나의 제출 경로에 메소드 방식은 여러 개 있을 수 있습니다. 예)

@app.route("/contact", methods=["GET", "POST"]

더 많은 정보는 아래 문서를 참고하세요.
[https://flask.palletsprojects.com/en/1.1.x/quickstart/#http-methods](.https://flask.palletsprojects.com/en/1.1.x/quickstart/#http-methods)


# 과제 4
플라스크에는 서버로 전송된 요청 매개변수를 활용할 수 있는 request 메소드(요청 모듈과 혼동하지 마세요)가 있습니다.

💪 어려운 과제: 아래 플라스크 문서를 참고하여, 양식에 입력된 이름과 비밀번호를 다시 클라이언트로 보내어 <h1>으로 출력하세요.