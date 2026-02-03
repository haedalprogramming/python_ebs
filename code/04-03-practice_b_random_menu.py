# 4차시 - 군집 자료형
# 실습 B
# 랜덤 모듈을 사용한 점심 메뉴 뽑기
# random 모듈을 import 해준다
import random
# menus에 ["김밥", "라면", "피자", "햄버거", "떡볶이"]리스트 저장
menus = ["김밥", "라면", "피자", "햄버거", "떡볶이"]
# "점심 메뉴 룰렛!" 출력
print("점심 메뉴 룰렛!")
# "후보: menus" 출력 
print(f"후보: {menus}")
# "엔터를 누르면 메뉴가 정해져요!" 출력후 입력값 기다림
input("엔터를 누르면 메뉴가 정해져요!")
# pick 변수에 menus에서 하나 고른 메뉴를 저장한다.
pick = random.choice(menus)
# "오늘의 메뉴: pick" 출력
print(f"🍽️ 오늘의 메뉴: {pick}")
