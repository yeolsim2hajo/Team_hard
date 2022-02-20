# 숫자 2개를 입력받아
# 첫 번째 숫자가 7이고, 두 번째 숫자가 9 이면 인증됨 출력
# 그렇지 않으면 재시도 출력

n1, n2 = map(int, input().split())

if n1 == 7 and n2 == 9:
    print("인증됨")
else:
    print("재시도")