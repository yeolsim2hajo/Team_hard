#아이디와 비밀번호 입력받기


# 숫자 2개를 입력받고,
# 아이디는 1111, 비밀번호는 2222를 입력해야 로그인 처리가 됨

# 아이디가 틀렸으면, 아이디가 틀렸습니다 출력
# 아이디는 맞지만, 비번이 틀리면 비밀번호가 틀렸습니다 출력
# 아이디와 비번이 모두 맞으면 '로그인성공' 출력


user_id, user_password = map(int, input().split())

id = 1111
password = 2222

if user_id != id:
    print('아이디가 틀렸습니다')
elif user_id == id and password != user_password:
    print('비밀번호가 틀렸습니다')
elif user_id == id and password == user_password:
    print('로그인성공')