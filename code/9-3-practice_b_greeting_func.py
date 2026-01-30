# 9차시 - 함수
# 실습 코드 B: 맞춤 인사 함수

# 실습 B
# 인사 함수
# moring_greet(name) 정의
def morning_greet(name):
    # "좋은 아침이에요, name님!" 반환
    return f"좋은 아침이에요, {name}님!"
# evening_greet(name) 정의
def evening_greet(name):
    # "좋은 저녁이에요, name님!" 반환
    return f"좋은 저녁이에요, {name}님!"
# birthday_greet(name,age)정의
def birthday_greet(name,age):
    # "name님, age살 생일 축하해요!" 반환
    return f"{name}님, {age}살 생일 축하해요!"
# moring_greet("철수") 출력
print(morning_greet("철수"))
# evening_greet("영희") 출력
print(evening_greet("영희"))
# birthday_greet("민수",15) 출력
print(birthday_greet("민수",15))
