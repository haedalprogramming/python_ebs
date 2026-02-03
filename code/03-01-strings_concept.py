# 3차시 - 문자열
# 개념 학습 코드: 텍스트 다루기, 인덱싱/슬라이싱

# 문자열 기본 예제
# msg1 변수에 문자열 저장
msg1 = "안녕하세요"   
# msg2 변수에 문자열 저장
msg2 = '반갑습니다'   
# msg1 msg2 출력
print(msg1, msg2)

# 여러 줄 문자열 저장 예제
# poem에 """장미는 빨갛고
# 제비꽃은 파랗다""" 저장
poem = """장미는 빨갛고
제비꽃은 파랗다"""
# poem 출력
print(poem)

# 문자열 더하기 예제
# first에 "파이"저장
first = "파이"
# second에 "썬"저장
second = "썬"
# first_second 출력
print(first + second)

# 문자열 반복 예제
# laugh에 "하"저장
laugh = "하"
# laugh 3번 출력
print(laugh * 3)

# len() 예제
# word 변수에 "Python" 저장
word = "Python"
# word 변수의 글자길이 출력
print(len(word))

# 인덱싱 예제
# word 변수에 "Python"저장
word = "Python"
# word의 0번째 출력
print(word[0])  # P
# word의 2번째 출력
print(word[2])  # t
# word의 5번째 출력
print(word[5])  # n

# 문자열 슬라이싱 예제
# word 변수에 "Python"저장
word = "Python"
# word의 0번부터 1번까지 출력
print(word[0:2])  # Py
# word의 2번부터 4번까지 출력
print(word[2:5])  # tho
# word의 전체 출력
print(word[:])    # Python

# 스탭과 뒤집기 예제
# word 변수에 "Python"저장
word="Python"
# word의 2간격으로 출력
print(word[::2])   # Pto
# word의 -1 간격(거꾸로) 출력
print(word[::-1])  # nohtyP

# 슬라이싱 연습 예제
# sentance 변수에 "Hello, World!" 저장
sentance="Hello, World!"
# sentance에서 4번까지 슬라이싱 (끝번호 5번은 포함안됨)
print(sentance[:5])
# sentance에서 7번부터 11번까지 슬라이싱 (끝번호 12번은 포함안됨)
print(sentance[7:12])
# sentance를 역순으로 슬라이싱
print(sentance[::-1])

# 문자열 메서드 예제
# msg에 "Hello World"저장
msg = "Hello World"
# msg를 모두 대문자로
print(msg.upper())
# msg를 모두 소문자로
print(msg.lower())
# msg에서 "World"를 "Python"으로
print(msg.replace("World", "Python"))		

# 포멧팅 예제
# name 변수에 "철수" 저장
name = "철수"
# age 변수에 15 저장
age = 15
# 이름: name값, 나이: age값 출력
print(f"이름: {name}, 나이: {age}")

