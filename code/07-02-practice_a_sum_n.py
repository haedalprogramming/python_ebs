# 7차시 - for 반복문
# 실습 코드 A: 1부터 n까지 합 구하기

# 실습 A 1부터 100까지의 합
# 합계를 저장할 변수 만들기
total = 0
# for문으로 숫자 더하기
for i in range(1, 101):
    total += i
# 결과 출력하기
print(f"합계: {total}")
#==================================================
# 실습 A 응용
# n까지 합 구하기
# 1부터 어디까지 더할지 물어보고 n변수에 저장하기
n=int(input("어디까지 더할까요? "))
# 합계를 저장할 total 변수 만들기
total=0
# for문으로 i를 1부터 n까지 n번 반복하기
for i in range(1,n+1):
    # total 변수에 i값 더하기
    total+=i
# 1부터 n까지의 합 total 출력하기
print(f"1부터 {n}까지 합: {total}")
