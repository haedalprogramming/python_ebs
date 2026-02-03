# 2차시 - 수치 자료형과 변수
# 개념 학습 코드: 숫자 다루기, 변수 개념

# 파이썬에서 숫자 써보기
# a에다가 10을 넣는다
a = 10 	# 정수
# b에다가 3.14를 넣는다
b = 3.14 	# 실수
# a와 b를 출력한다.
print(a, b)

# 자료형 확인하기
# 10의 형식을 출력한다
print(type(10)) 		#<class ‘int’>
# 3.14의 형식을 출력한다.
print(type(3.14)) 	#<class ‘float’>

# 몫과 나머지 연산자
# 7나누기 2의 몫을 출력
print(7 // 2) 	# 3
# 7나누기 2의 나머지를 출력
print(7 % 2)	# 1

# 연산자 예제
# x에 7을 저장
x = 7
# y에 2를 저장
y = 2
# x더하기 y 출력 
print(x + y)   # 9
# x곱하기 y출력
print(x * y)   # 14
# x 나누기 y출력
print(x / y)   # 3.5
# x 나누기 y의 몫 출력
print(x // y)  # 3
# x 나누기 y의 나머지 출력
print(x % y)   # 1

# name 변수에 “철수”문자열 저장
name = "철수" # 문자열
# age 변수에 15 정수 저장
age = 15        # 정수
# height 변수에 165.5 실수 저장
height = 165.5  # 실수

# price 변수에 1000저장
price = 1000
# count 변수에 3 저장
count = 3
# total 변수에 price 곱하기 total값 저장
total = price * count
# total 값 출력하기
print(total)  # 3000

# score변수에 80 저장
score = 80
# score 변수 출력
print(score)  # 80
# score 변수에 90 저장
score = 90    # 새 값으로 덮어쓰기
# sore 변수 출력
print(score)  # 90
