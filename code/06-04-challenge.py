# 6차시 - 조건문
# 도전 과제
# 요금 계산기
# "나이를 입력하세요: " 다음에 입력되는 정수값을 age에 저장
age = int(input("나이를 입력하세요: "))
# 만약 age가 7보다 작거나 같다면
if age <= 7:
	# price에 0 저장
    price = 0
# 아니면서 만약 age가 13보다 작거나 같다면
elif age <= 13:
	# price에 500 저장
    price = 500
# 아니면서 만약 age가 19보다 작거나 같다면
elif age <= 19:
	# price에 1000 저장
    price = 1000
# 아니면
else:
	# price에 2000 저장
    price = 2000
# price 요금 출력
print(f"요금: {price}원")
