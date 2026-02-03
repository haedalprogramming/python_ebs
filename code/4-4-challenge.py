# 4차시 - 군집 자료형
# 도전과제
# 숫자 5개를 리스트에 저장하고 합계와 평균을 구하기
# nums에 빈 리스트를 저장.
nums = []
# 변수 i를 0부터 4까지 1씩 증가시키며 5번 반복
for i in range(5):
	# "i+1번째 숫자: " 뒤에 입력되는 값을 정수로 n변수에 저장한다.
    n = int(input(f"{i+1}번째 숫자: "))
	# nums 리스트에 n 추가
    nums.append(n)
# "합계: sum(nums)" 출력
print(f"합계: {sum(nums)}") 
# "평균: sum(nums)/len(nums)" 출력
print(f"평균: {sum(nums)/len(nums)}") 

