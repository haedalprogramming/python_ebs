# 4차시 - 군집 자료형
# 개념 학습 코드: 리스트, 튜플 등 데이터 묶음

# 리스트 만들기 예제
# fruits에 ["사과","바나나","오렌지"] 리스트 저장
fruits = ["사과", "바나나", "오렌지"]

# numbers에 [1,2,3,4,5] 리스트 저장 
numbers = [1, 2, 3, 4, 5]

# mixed에 [1,"hello",3.14,True] 리스트 저장
mixed = [1, "hello", 3.14, True]

# 리스트 인덱싱 예제
# fruits에 ["사과", "바나나", "오렌지"]리스트 저장
fruits = ["사과", "바나나", "오렌지"]
# fruits의 0번째 출력
print(fruits[0])   
# fruits의 1번째 출력
print(fruits[1])
# fruits의 -1번째 출력   
print(fruits[-1])  

# nums에 [10,20,30,40,50] 리스트 저장
nums = [10, 20, 30, 40, 50]
# nums의 1번부터 3번까지 출력
print(nums[1:4])   
# nums의 2번까지 출력
print(nums[:3])    
# nums를 2개 간격으로 출력
print(nums[::2]) 

# 리스트 길이와 포함 여부 예제
# fruits에 ["사과", "바나나", "오렌지"]리스트 저장
fruits = ["사과", "바나나", "오렌지"]
# fruits의 길이 출력
print(len(fruits))     
# fruits에 "사과" 포함여부 출력   
print("사과" in fruits)  
# fruits에 "포도" 포함여부 출력   
print("포도" in fruits)   # False(포함여부)

# 리스트 수정하기 예제
# fruits에 ["사과", "바나나", "오렌지"]리스트 저장
fruits = ["사과", "바나나", "오렌지"]
# fruits의 1번째 자리를 포도로 바꾸기
fruits[1] = "포도"  
# fruits 출력
print(fruits)

# 리스트에 추가하기 예제
# fruits에 ["사과","바나나"] 리스트 저장
fruits = ["사과", "바나나"]
# fruits 리스트에 "오렌지" 맨뒤에 추가
fruits.append("오렌지")  
# fruits 리스트 출력
print(fruits)  
# fruits 1번 자리에 "포도" 삽입
fruits.insert(1, "포도")  
# fruits 리스트 출력
print(fruits)

# 리스트에서 삭제하기 예제
# fruits에 ["사과", "바나나", "오렌지"]리스트 저장
fruits = ["사과", "바나나", "오렌지"]
# fruits리스트에서 "바나나"삭제
fruits.remove("바나나") 
# fruits 리스트 출력
print(fruits)  
# fruits 리스트에서 맨 뒤에 값을 삭제해서 last에 저장
last = fruits.pop()  
# last값 출력
print(last)    
# fruits 리스트 출력
print(fruits)  

# 리스트 정렬하기 예제
# nums에 [3,1,4,1,5] 리스트 저장
nums = [3, 1, 4, 1, 5]
# nums 리스트 오름차순 정렬
nums.sort()   
# nums 리스트 출력  
print(nums)     
# nums 리스트 순서 뒤집기
nums.reverse()  
# nums 리스트 출력
print(nums)

# 유용한 리스트 메서드 예제
# nums에 [1,2,3,2,1] 리스트 저장
nums = [1, 2, 3, 2, 1]
# nums에 2가 몇개인지 출력
print(nums.count(2))  
# nums에서 3의 위치 출력
print(nums.index(3))  
# nums 리스트에 있는 값들 모두 삭제
nums.clear()       
# nums 리스트 출력   
print(nums) 

# 튜플 연습 예제
# colors에 ("빨강", "파랑", "초록") 튜플 저장
colors = ("빨강", "파랑", "초록")
# point에 (10,20) 튜플 저장
point = (10, 20)      
# single에 (42,) 튜플 저장(요소 1개일 때도 쉼표 필수)
single = (42,) 
# colors 튜플의 0번째 값 출력       
print(colors[0]) 

