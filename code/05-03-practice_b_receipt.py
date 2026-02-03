# 5차시 - 문자 입출력

# 실습 B
# 영수증 출력 프로그램
print("=== 편의점 영수증 ===")
# "상품1 이름: " 뒤에 입력하는 값을 item1에 저장
item1 = input("상품1 이름: ")
# "상품1 가격: " 뒤에 입력하는 값을 price1에 저장
price1 = int(input("상품1 가격: "))
# "상품2 이름: " 뒤에 입력하는 값을 item2에 저장
item2 = input("상품2 이름: ")
# "상품2 가격: " 뒤에 입력하는 값을 price2에 저장
price2 = int(input("상품2 가격: "))

print("\n" + "=" * 30)
print("        [ 영수증 ]")
print("=" * 30)
# "item1 왼쪽으로 15칸 정렬 price1 오른쪽으로 10칸 정렬 원" 출력
print(f"{item1:<15}{price1:>10,}원")
# "item2 왼쪽으로 15칸 정렬 price2 오른쪽으로 10칸 정렬 원" 출력
print(f"{item2:<15}{price2:>10,}원")
print("-" * 30)
# total 변수에 price1+price2 값 저장
total = price1 + price2
# "합계 왼쪽으로 15칸 정렬 total 오른쪽으로 10칸 정렬 원" 출력
print(f"{'합계':<15}{total:>10,}원")
print("=" * 30)
