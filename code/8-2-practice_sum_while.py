# 8차시 - while 반복문
# 실습 코드 A: while로 n초 카운트다운하기

# 실습 예제 A
# 카운트다운 코드

# time 모듈 불러오기
import time
# "몇 초부터? "뒤에 입력하는 값을 정수로 변수 n에 저장
n = int(input("몇 초부터? "))
# n이 0보다 큰동안 반복
while n > 0:
	# n 출력
    print(n)
	# 1초 기다리기
    time.sleep(1)
	# n값을 1감소
    n -= 1
# "끝!" 출력
print("끝!")
#==================================================
# 실습 예제 A 응용
# 카운트다운 코드 분:초
# time 모듈 불러오기
import time
# "총 몇 초? "뒤에 입력하는 값을 정수로 변수 seconds에 저장
seconds=int(input("총 몇 초? "))
# seconds가 0보다 클때 반복
while seconds>0:
    # mins에 seconds를 60으로 나눈 몫 저장
    mins=seconds//60
    # secs에 seconds를 60으로 나눈 나머지 저장
    secs=seconds%60
    # mins와 secs둘다 두 자리로 빈자리 0으로 정수로 출력
    print(f"{mins:02d}:{secs:02d}")
    # 1초 기다리기
    time.sleep(1)
    # seconds 값 1 감소
    seconds -=1
# "타이머 종료!" 출력
print("타이머 종료!")
