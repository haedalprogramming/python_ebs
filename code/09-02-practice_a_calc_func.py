# 9차시 - 함수
# 실습 코드 A: 사칙연산 함수 계산기

# 실습 A
# 각각의 사친연산을 함수로 만들기
# add(a,b) 정의
def add(a,b):
    # a+b로 반환
    return a+b
# sub(a,b) 정의
def sub(a,b):
    # a-b로 반환
    return a-b
# mul(a,b) 정의
def mul(a,b):
    # a*b로 반환
    return a*b
# div(a,b) 정의
def div(a,b):
    # 만약에 b가 0이라면
    if b==0:
        # "0으로 나눌 수 없어요!"로 반환
        return "0으로 나눌 수 없어요!"
    # a/b로 반환
    return a/b
# x,y에 10,3 저장
x,y=10,3
# x+y=add(x,y) 출력
print(f"{x}+{y}={add(x,y)}")
# x-y=sub(x,y) 출력
print(f"{x}-{y}={sub(x,y)}")
# x*y=mul(x,y) 출력
print(f"{x}*{y}={mul(x,y)}")
# x/y=div(x,y)(소수점 둘째 자리까지) 출력
print(f"{x}/{y}={div(x,y):.2f}")

# 실습 A 확장
# 기존에 만든 add,sub,mul,div 함수를 관리하는 함수
# calc(a,b,op)정의
def calc(a,b,op):
    # 만약에 op변수값이 "+"라면
    if op=="+":
        # add(a,b)값을 반환
        return add(a,b)
    # 만약에 op변수값이 "-"라면
    if op=="-":
        # sub(a,b)값을 반환
        return sub(a,b)
    # 만약에 op변수값이 "*"라면
    if op=="*":
        # mul(a,b)값을 반환
        return mul(a,b)
    # 만약에 op변수값이 "/"라면
    if op=="/":
        # div(a,b)값을 반환
        return div(a,b)
# calc(5,3,"+") 출력
print(calc(5,3,"+"))
