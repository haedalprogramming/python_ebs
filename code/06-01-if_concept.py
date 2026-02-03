# 6차시 - 조건문
# 개념 학습 코드: if, elif, else

# 비교 연산자 예제
# a에 10 저장
a = 10
# b에 5 저장
b = 5
# a는 b와 같은가요? 출력
print(a == b)			# False
# a는 b와 다른가요? 출력
print(a != b)			# True
# a는 b보다 큰가요? 출력
print(a > b)			# True
# a는 10보다 크거나 같나요? 출력
print(a >= 10)			# False

# 등호 한개와 두개 차이 예제
# x에 5를 저장하겠다
x = 5      # 저장
# x랑 5랑 같은가요?
x == 5     # 비교

# 문자열 비교 예제
# name에 철수 저장
name = "철수"
# name 값과 "철수"가 같은가요? 출력
print(name == "철수")  # True
# name 값과 "영희"가 같은가요? 출력
print(name == "영희")  # False

# if문 기본 예제
# age에 15저장
age = 15
# 만약 age가 13보다 크거나 같다면
if age >= 13:
	# "청소년입니다!'라고 출력
    print("청소년입니다!")

# if else 문 예제
# score에 75 저장
score = 75
# 만약 score가 60보다 크거나 같다면
if score >= 60:
	# "합격!"출력
    print("합격!")
# 아니라면
else:
	# "불합격..." 출력
    print("불합격...")

# elif 문 예제
# score에 85 저장
score = 85
# 만약 score가 90보다 크거나 같다면
if score >= 90:
	#"A" 출력
    print("A")
# 아니면서 만약 80보다 크거나 같다면
elif score >= 80:
	# "B" 출력
    print("B")
# 아니면서 만약 70보다 크거나 같다면
elif score >= 70:
	# "C"출력
    print("C")
# 아니면
else:
	# "F"출력
    print("F")

# and 연산자 예제
# age에 20 저장
age = 20
# has_id에 True 저장
has_id = True
# 만약 age가 19보다 크거나 같고 그리고 has_id라면(True라면)
if age >= 19 and has_id:
	# "입장 가능!" 출력
    print("입장 가능!")

# or 연산자 예제
# day에 "토요일" 저장
day = "토요일"

# 만약에 day값이 "토요일" 또는 "일요일"이라면
if day == "토요일" or day == "일요일":
	# "주말이다!" 출력
    print("주말이다!")

# not 연산자 예제
# is_raining에 False 저장
is_raining = False
# 만약 is_raining이 아니라면(is_raining이 False라면)
if not is_raining:
	# "산책 가자" 출력
    print("산책 가자!")


