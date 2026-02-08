# 2차시 - 수치 자료형과 변수
# 실습 코드 A: 간단 계산기

# 실습 A
# 사칙연산 계산기
#num1 변수에 첫번째 숫자를 정수로 입력받기
num1 = int(input("첫 번째 숫자: "))
#num2 변수에 두번째 숫자를 정수로 입력받기
num2 = int(input("두 번째 숫자: "))

# add변수에 num1 더하기 num2값 저장하기
add = num1 + num2
# sub 변수에 num1 빼기 num2값 저장하기
sub = num1 - num2
# mul 변수에 num1 곱하기 num2값 저장하기
mul = num1 * num2
# div 변수에 num1 나누기 num2값 저장하기
div = num1 / num2

#더하기값 출력하기
print("더하기:", add)
# 빼기 값 출력하기
print("빼기:", sub)
# 곱하기값 출력하기
print("곱하기:", mul)
# 나누기 값 출력하기
print("나누기:", div)
