# 6차시 - 조건문
# 실습 코드 A: 성적 판별기

# "점수를 입력하세요: "뒤에 입력되는 값을 정수로 score에 저장
score = int(input("점수를 입력하세요: "))
# 만약 score가 90이상이라면
if score >= 90:
    # grade에 "A"저장
    grade = "A"
# 아니면서 만약 score가 80 이상이라면
elif score >= 80:
    # grade에 "B"저장
    grade = "B"
# 아니면서 만약 score가 70 이상이라면
elif score >= 70:
    # grade에 "C"저장
    grade = "C"
# 아니면서 만약 score가 60 이상이라면
elif score >= 60:
    # grade에 "D"저장
    grade = "D"
# 아니면
else:
    # grade에 "F"저장
    grade = "F"
# "당신의 학점은 grade입니다!" 출력
print(f"당신의 학점은 {grade}입니다!")
