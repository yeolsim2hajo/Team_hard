# 비밀번호 맞추기
# 숫자 4개를 입력받아라
# 비밀번호는 1 2 3 4
# 비밀번호가 맞다면 로그인 성공
# 그렇지 않으면 로그인 실패
password_original = [1,2,3,4]
password = list(map(int, input().split()))
cnt = 0
for i in range(4):
    if password[i] == password_original[i]:
        cnt += 1
if cnt == 4:
    print('로그인성공')
else:
    print('로그인실패')

