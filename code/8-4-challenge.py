# 8차시 - while 반복문
# 도전 과제

# 도전과제
# 숫자 스무고개
# random 모듈 불러오기
import random
# randNum에 1부터 10사이 정수 저장하기
randNum=random.randint(1,10)
# "컴퓨터가 1부터 10사이 랜덤한 숫자를 생각했습니다." 출력
print("컴퓨터가 1부터 10사이 랜덤한 숫자를 생각했습니다.")
# 무한 반복
while True:
    # 일단 시도
    try:
        # "1~10사이 숫자를 맞춰보세요!" 뒤에 입력되는 값을 guess변수에 저장
        guess=int(input("1~10사이 숫자를 맞춰보세요!"))
        # 만약 guess 변수 값이 1보다 크거나 같고 10보다 작거나 같다면
        if 1<=guess<=10:
            # 만약 guess 변수값이 randNum변수 값과 같다면
            if guess==randNum:
                # "정답입니다! 정답은 guess입니다." 출력
                print(f"정답입니다! 정답은 {guess}입니다")
                # 반복중단
                break
            # 아니라면
            else:
                # "오답입니다! 정답은 guess가 아닙니다." 출력
                print(f"오답입니다! 정답은 {guess}가 아닙니다.")
        # 아니라면(입력한 숫자가 1~10사이 숫자가 아니라면)
        else:
            #"1~10사이 숫자를 입력해주세요." 출력
            print("1~10사이 숫자를 입력해주세요")
    # ValueError라면(정수가 아니라면)
    except ValueError:
        # "숫자를 입력하세요!" 출력
        print("숫자를 입력하세요!")


