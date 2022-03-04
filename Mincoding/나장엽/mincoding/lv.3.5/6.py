# 계산하고 검사하기
# 숫자 두개를 입력 받고
# 두 숫자의 곱이 30~50 사이 이면 적당한 사이즈 출력
# 50보다 같거나 크면 큰 사이즈 출력
# 30보다 같거나 작으면 작은 사이즈 출력


n1, n2 = map(int, input().split())
result = n1*n2

if 30 <= result <= 50:
    print('적당한 사이즈')
elif result >= 50:
    print('큰 사이즈')
elif result <= 30:
    print('작은 사이즈')


