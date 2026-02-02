# 2차시 - 수치 자료형과 변수
# 도전 과제

# radius 변수에 실수로 반지름을 입력받는다
radius = float(input("반지름: "))
# pi변수에 3.14159를 저장한다
pi = 3.14159
# area 변수에 pi 곱하기 반지름의 제곱값을 저장한다
area = pi * radius ** 2
# area를 소수 둘째 자리까지 출력한다.
print("원의 넓이:", round(area, 2))

