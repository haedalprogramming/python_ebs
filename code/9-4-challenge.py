# 9차시 - 함수
# 도전 과제

# 도전과제
# bmi 함수
# calc_bmi(weight,height)의 정의
def calc_bmi(weight,height):
    # bmi 변수에 weight값을 height의 제곱으로 나눈 값 저장
    bmi=weight/(height**2)
    # bmi 변수 소수점 한자리까지만 반환
    return round(bmi,1)
# calc_bmi(70,1.75) 출력
print(calc_bmi(70,1.75))
