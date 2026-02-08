# 2차시 - 수치 자료형과 변수
# 실습 코드 B: BMI 측정기

# 실습 B
# BMI 계산기

# weight 변수에 몸무게(kg) 실수값 입력받기
weight = float(input("몸무게(kg): "))
# height 변수에 키(m) 실수값 입력받기
height = float(input("키(m): "))
# bmi 변수에 weight를 height의 제곱으로 나눈값 저장히기
bmi = weight / (height ** 2)

# bmi 출력하기
print("당신의 BMI:", bmi)
# 반올림한 bmi출력하기
print("반올림:", round(bmi, 1))
