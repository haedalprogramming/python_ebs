# 10차시 - 개념 복습
# 퀴즈 6개

# 퀴즈 1
# 리스트의 슬라이싱 복습
# nums리스트에 [1,2,3,4,5] 저장
nums=[1,2,3,4,5]
# nums리스트의 1번 항목부터 3번 항목까지(마지막 숫자는 포함안됨) 출력
print(nums[1:4])
# nums[1]=2, nums[3]=4 이므로 정답은 B)[2,3,4]

# 퀴즈 2
# for 반복문 range(시작, 끝, 간격)
# i변수를 1부터 6까지 2씩 증가시키면서 반복
for i in range(1, 6, 2):
	# i 출력
print(i)
# 1 3 5이므로 정답은 B(1 3 5)

# 퀴즈 3
# 함수와 매개변수, 기본값
# test(a, b=10(기본값))정의하기
def test(a,b=10):
	# a*b 반환하기
	return a*b
# test(5) 출력하기
print(test(5))
# 인수값이 2개 전달되어야 하지만 1개만 전달됨. 하지만 b=10기본값이 있어서 
# a=5, b=10, a*b=50으로 정답은 C)50

# 퀴즈 4
# 연산자 복습
# numbers에 [1,2,3,4,5]저장
numbers=[1,2,3,4,5]
# total 변수에 0저장
total=0
# numbers에 있는 값들을 하나씩 꺼내서 n에 넣고
for n in numbers:
	# total에 total+n값 저장하기
	total +=n
# total값 출력
print(total)
# 빈칸에 들어갈 연산자는 복합대입연산자 += 

# 퀴즈 5
# 리시트 복습
# fruits 리스트에 "사과","바나나" 저장. 
fruits=["사과","바나나"]
# fruits 리스트에 "오렌지" 맨뒤에 추가
fruits.append("오렌지")
# fruits의 길이 출력
print(len(fruits))
# ["사과","바나나"]리스트에 "오렌지"를 추가했으므로 ["사과","바나나","오렌지"]
# 따라서 fruits 리스트의 길이는 3. 출력 결과도 3이다.

# 퀴즈 6
# 함수 복습
# greeting(name) 정의하기
def greeting(name): # :이 빠지면 SyntaxError가 발생
	# "안녕, name" 출력
# greeting("철수") 호출
greeting("철수")

