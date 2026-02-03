# 7차시 - for 반복문
# 실습 코드 B: 구구단

# 실습 B 구구단 출력기
# 출력할 단수 정수로 dan에 입력받기
dan = int(input("몇 단? "))
print(f"=== {dan}단 ===")
# i변수를 1부터 9까지 증가시키면서 9번 반복
for i in range(1, 10):
	# 내가선택한 단수 X i=dan*i 출력하기 
    print(f"{dan} x {i} = {dan * i}")
#==================================================
# 실습 B 응용. 구구단 전체 출력기
# dan 변수를 2부터 9까지 증가시키면서 8번 반복
for dan in range(2,10):
    # 출력할 단수 출력
    print(f"=== {dan}단 ===")
    # i 변수를 1부터 9까지 증가시키면서 9번 반복
    for i in range(1,10):
        # dan X i = dan*i 출력
        print(f"{dan}X{i}={dan*i}")
    # 한 단마다 한줄 엔터
    print()
