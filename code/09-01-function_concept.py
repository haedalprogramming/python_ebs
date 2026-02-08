# 9차시 - 함수
# 개념 학습 코드: def 정의와 호출

# 여러줄 함수 예제
# introduce() 함수를 정의
def introduce():
    # "="20번 출력
    print("=" * 20)
    # "안녕하세요!" 출력
    print("안녕하세요!")
    # "저는 파이썬입니다" 출력
    print("저는 파이썬입니다.")
    # "="20번 출력
    print("=" * 20)
# introduce()함수 호출
introduce()
#==================================================
# 매개변수 여러개 예제
# add(a,b) 정의하기
def add(a, b):
    # "a+b=(a+b)" 출력
    print(f"{a} + {b} = {a + b}")
# add(3,5) 호출
add(3, 5)
# add(10,20) 호출
add(10, 20)
#==================================================
# 기본값 설정 예제
# greet(name, msg="안녕하세요"(기본값)) 함수 정의
def greet(name, msg="안녕하세요"):
    #"name님, msg!" 출력
    print(f"{name}님, {msg}!")
# greet("철수") 호출(msg에 기본값 "안녕하세요"가 있어서 생략)
greet("철수")
# greet("영희","반가워요") 호출
greet("영희", "반가워요")
#==================================================
# 키워드 인수 예제
# info(name,age,city) 정의
def info(name, age, city):
    # "name,age살,city" 출력
    print(f"{name}, {age}살, {city}")
# info(age=20,city="서울",name="민수")호출
# 키워드를 사용해서 순서와 상관없이 값 전달 가능
info(age=20, city="서울", name="민수")
#==================================================
# return 활용 예제
# square(n) 정의(square: 제곱이라는 뜻)
def square(n):
    # n**2(n을 2번 곱한값)으로 반환
    return n ** 2
# x변수에 square(4) 저장 (4X4=16)
x = square(4)  
# y변수에 square(5) 저장 (5X5=25)
y = square(5)  
# x+y 출력 (41)
print(x + y)  
#==================================================
# return 여러값 예제
# calc(a,b)정의하기
def calc(a, b):
    # a+b, a-b, a*b, a/b 값으로 반환하기
    return a + b, a - b, a * b, a / b
# add, sub, mul, div 변수에 calc(10,3)에서 반환하는 값들 저장
add, sub, mul, div = calc(10, 3)
# add, sub, mul, div 출력
print(add, sub, mul, div)
# 13 7 30 3.333...
#==================================================
# print와 return 비교 예제
# add1(a,b) 정의
def add1(a, b):
    # a+b 출력
    print(a+b)

# add2(a,b) 정의
def add2(a, b):
    # a+b 반환
    return a + b
# result1에 add1(1,2)값 저장
# add1(1,2)가 호출되서 3이 출력되지만 result1에 저장되는건 없음
result1 = add1(1, 2)
# result2에 add2(1,2)값 저장
# a+b값을 반환했으므로 3이 저장
result2 = add2(1, 2)
print("="*30)
# result1 출력. result1에 저장된게 없어서 None
print(result1)
# result2 출력. 반환한 값이 3 출력
print(result2)
