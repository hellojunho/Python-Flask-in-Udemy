# question_model.py 구현
[요구사항]
1. Question 클래스 생성
2. __init__() 생성자 사용
3. attributes:{{"text"}, {"answer"}}
    ex) new_q = Question("2+3=5", "True")

[모델링 완성]
```commandline
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
```

# main.py > question_bank 구현
data.py에 있는 question_data의 값들을 
반복문을 통하여 새로운 리스트인 question_bank에 {"text":"answer"}형식으로 저장

```commandline
from question_model import Question
from data import question_data

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]

    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# question_bank의 0번째 데이터의 answer값 출력
print(question_bank[0].answer)


```

# quiz_brain.py 구현
질문에 대답하도록 요구하는 파일 작성  
모든 질문과 대답하는 기능

[요구사항]
1. TODO: 질문
2. TODO: 대답이 맞는지 확인
3. TODO: 퀴즈의 마지막 단계까지 왔는지 확인
4. attributes: {{question_number = 0}, {questions_list}}

```commandline
class QuizBrain:
    def __init__(self, question_lists):
        self.question_number = 0
        self.question_lists = question_lists
```

# main.py > next_question() 구현
```commandline
    def next_question(self):
        current_question = self.question_lists[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text} (True/False): ")

```

# Open Trivia Database
[OPEN TRIVIA DATABASE](https://opentdb.com/)
많은 양의 검증된 퀴즈들이 있음.  
우측 상단 메뉴바에서 `API`클릭하면 
카테고리, 퀴즈 형식(o/x 등..), 난이도 등을 조절하여 퀴즈를 생성할 수 있음.  
모두 설정하면 `GENERAL API URL`클릭하고 해당 url로 들어가 json파일을 가져오면 끝!