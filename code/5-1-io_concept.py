# 5차시 - 문자 입출력
# 개념 학습 코드: input, print 포맷팅

# input 예제
# "이름이 뭐에요?" 뒤에 입력하는 값을 name 변수에 저장
name = input("이름이 뭐예요? ")
# f-string 으로 "안녕, {name}!"" 출력
print(f"안녕, {name}!")

# input()의 중요한 특징 예제
# "나이: " 뒤에 입력하는 값을 age 변수에 저장
age = input("나이: ")
# age의 type 출력
print(type(age))

# 형 변환 예제1
# "나이: "뒤에 입력하는 값을 age에 정수로 저장
age = int(input("나이: "))
# "키: "뒤에 입력하는 값을 height에 실수로 저장
height = float(input("키: "))

# 형 변환 예제 2
# "첫 번째 숫자: " 뒤에 입력되는 값을 정수형으로 num1에 저장
num1 = int(input("첫 번째 숫자: "))
# "두 번째 숫자: " 뒤에 입력되는 값을 정수형으로 num2에 저장
num2 = int(input("두 번째 숫자: "))
# "합: num1+num2" 출력
print(f"합: {num1 + num2}")

# print() 여러값 출력 예제
# name 변수에 "철수" 저장
name = "철수"
# age 변수에 15저장
age = 15
# name과 age 출력
print(name, age)
# name과 age 출력 구분자(sep)를 ", "으로
print(name, age, sep=", ")

# 줄바꿈 제어 예제
# "Hello"출력. 출력의 끝(end)을 " "(스페이스바)로
print("Hello", end=" ")
# "World"출력
print("World")		

# 이스케이프 문자 예제
# 문자열 중간에 줄바꿈(\n)
print("안녕\n하세요")
# 문자열 중간에 탭(\t)
print("탭\t간격")
# 문자열 중간에 따옴표(\\)
print("따옴표: \"\"")

# f-string 복습 예제
# name에 "영희"저장
name = "영희"
# score에 95저장
score = 95
# "name의 점수: score점" 출력
print(f"{name}의 점수: {score}점")
# "성취도: (score/100)*100 소수점 1자리까지%" 출력
print(f"성취도: {(score/100)*100:.1f}%")

# 정렬하기 예제
# f-string으로 10칸에서 왼쪽 정렬
print(f"{'왼쪽':<10}|")
# f-string으로 10칸에서 가운데 정렬
print(f"{'가운데':^10}|")
# f-string으로 10칸에서 오른쪽 정렬
print(f"{'오른쪽':>10}|")

# 숫자 포맷팅 예제
# price에 1234567저장
price = 1234567
# price를 천 단위 쉼표로 출력
print(f"{price:,}원")  
# pi에 3.141592 저장
pi = 3.141592
# pi를 소수점 둘째자리까지만 출력
print(f"{pi:.2f}")    









