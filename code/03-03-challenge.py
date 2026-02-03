# 3차시 - 문자열

# 도전과제
# 이메일 주소에서 아이디만 추출
# "이메일: "뒤에 입력되는값을 email에 저장
email = input("이메일: ")
# pos 변수에 email에서 "@"의 위치 저장
pos = email.find("@")
# user_id 변수에 email에서 "@"앞까지 저장
user_id = email[:pos]
# "아이디: user_id" 출력
print(f"아이디: {user_id}")


