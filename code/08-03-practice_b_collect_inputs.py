# 8차시 - while 반복문
# 실습 코드 B: 점수 모아서 통계 출력하기

# 실습 예제 B
# 점수 입력기
# scores에 빈 리스트 저장
scores = []
# "점수를 입력하세요 (끝: 'q')" 출력
print("점수를 입력하세요 (끝: 'q')")

# 무한 반복
while True:
	# "점수: "뒤에 입력되는 값을 data에 저장
    data = input("점수: ")
	# 만약에 data 값이 'q'와 같다면
    if data == 'q':
		# 반복 중단
        break
	# data 값을 정수로 scores 리스트에 추가
    scores.append(int(data))
# 만약에 scores 리스트의 길이가 0보다 크다면
if len(scores) > 0:
	# 전체 리스트 출력
    print(f"입력된 점수: {scores}")
	# 학생 수 출력
    print(f"학생 수: {len(scores)}명")
	# 총점 출력
    print(f"총점: {sum(scores)}점")
	# 평균 출력
    print(f"평균: {sum(scores)/len(scores):.1f}점")
	# 최고점 출력
    print(f"최고점: {max(scores)}점")
	# 최저점 출력
    print(f"최저점: {min(scores)}점")
# 아니면
else:
	# "입력된 점수가 없습니다" 출력
    print("입력된 점수가 없습니다.")
#==================================================
# 실습 예제 B 응용.
# 점수 입력기
# 이상한 값 거르기
# scores에 빈 리스트 저장
scores=[]
# "점수를 입력하세요 (끝: 'q')" 출력
print("점수를 입력하세요 (끝: 'q')")
# 무한 반복
while True:
    # "점수: "뒤에 입력되는 값을 data에 저장
    data=input("점수: ")
    # 만약에 data 값이 'q'와 같다면
    if data=='q':
        # 반복 중단
        break
    # 먼저 시도 한다
    try:
        # 변수 score에 data 정수 값을 저장
        score=int(data)
        # 만약에 socre가 0보다 크거나 같으면서 그리고
        # 100보다 작거나 같다면
        if 0<=score<=100:
            # score값을 scores리스트에 추가
            scores.append(score)
        # 아니면
        else:
            # "0~100 사이로 입력하세요" 출력
            print("0~100 사이로 입력하세요")
    # ValueError 문제가 생겼다면
    except ValueError:
        # "숫자를 입력하세요!" 출력
        print("숫자를 입력하세요!")
# 만약에 scores 리스트의 길이가 0보다 크다면
if len(scores)>0:
    # 전체 리스트 출력
    print(f"입력된 점수: {scores}")
    # 학생 수 출력
    print(f"학생 수: {len(scores)}명")
    # 총점 출력
    print(f"총점: {sum(scores)}점")
    # 평균 출력
    print(f"평균: {sum(scores)/len(scores):.1f}점")
    # 최고점 출력
    print(f"최고점: {max(scores)}점")
    # 최저점 출력
    print(f"최저점: {min(scores)}점")
# 아니면
else:
    # "입력된 점수가 없습니다" 출력
    print("입력된 점수가 없습니다")
