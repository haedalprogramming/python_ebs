# 10차시 - 개념 복습
# 도전 과제

# 도전과제
# 학생들의 점수를 입력받아 통계를 내는 프로그램
# get_scores() 함수 정의하기
def get_scores():
    # scores에 빈 리스트 저장
    scores=[]
    # 무한 반복
    while True:
        # "점수 (q=종료)" 뒤에 입력되는 값을 data에 저장
        data=input("점수 (q=종료): ")
        # 만약 data값이 'q'라면
        if data=='q':
            # 반복 중단
            break
        # scores 리스트에 data를 정수형으로 추가
        scores.append(int(data))
    # scores 리스트로 반환
    return scores

# calc_stats(scores) 정의하기
def calc_stats(scores):
    # 만약 scores 리스트의 길이가 0이라면
    if len(scores)==0:
        # None으로 반환
        return None
    # total 변수에 scores의 총합 저장
    total=sum(scores)
    # avg에 total 나누기 scores 리스트의 길이 저장
    avg=total/len(scores)
    # total,avg,scores 최대값, scores 최소값 반환
    return total,avg,max(scores),min(scores)

# get_grade(avg) 정의
def get_grade(avg):
    # 만약 avg가 90이상이라면
    if avg>=90:
        # "A" 반환
        return "A"
    # 아니면서 만약 avg가 80이상이라면
    elif avg>=80:
        # "B" 반환
        return "B"
    # 아니면서 만약 avg가 70이상이라면
    elif avg>=70:
        # "C" 반환
        return "C"
    # 아니면서 만약 avg가 60이상이라면
    elif avg>=60:
        # "D" 반환
        return "D"
    # 아니면
    else:
        # "F" 반환
        return "F"
print("=== 성적 관리 프로그램 ===")
# scores에 함수 get_scores() 반환값 저장
scores=get_scores()
# 만약 scores에 값이 있다면
if scores:
    # total, avg, max_s, min_s에 calc_stats(scores)반환값을 저장
    total,avg,max_s,min_s=calc_stats(scores)
    # grade에 get_grade(avg)값 저장
    grade=get_grade(avg)
    # "총점: total점" 출력
    print(f"\n총점: {total}점")
    # "평균: avg(소수점 1자리)점" 출력
    print(f"평균: {avg:.1f}점")
    # "최고: max_s점, 최저: min_s점" 출력
    print(f"최고: {max_s}점, 최저: {min_s}점")
    # "학점: grade" 출력
    print(f"학점: {grade}")
