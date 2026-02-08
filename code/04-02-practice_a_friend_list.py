# 4차시 - 군집 자료형

# 실습 A
# 친구 목록 관리 프로그램
# friends에 ["철수","영희","민수"] 리스트 저장
friends = ["철수", "영희", "민수"]
# "내 친구들: friends" 출력
print(f"내 친구들: {friends}")
# "총 len(friends)명" 출력
print(f"총 {len(friends)}명")
# "새 친구 이름: " 뒤에 입력값을 new_friend에 저장
new_friend = input("새 친구 이름: ")
# friends 리스트에 new_friend 추가
friends.append(new_friend)
# "친구 추가 완료: friends" 출력
print(f"친구 추가 완료: {friends}")
# "삭제할 친구: " 뒤에 입력값을 bye_friend에 저장
bye_friend = input("삭제할 친구: ")
# 만약 bye_friend 값이 friends 리스트에 존재한다면
if bye_friend in friends:
	# friends 리스트에서 bye_friend값 삭제
    friends.remove(bye_friend)
	# "bye_friend 삭제 완료!" 출력
    print(f"{bye_friend} 삭제 완료!")
# 아니면
else:
	# "그런 친구 없어요..." 출력
    print("그런 친구 없어요...")
