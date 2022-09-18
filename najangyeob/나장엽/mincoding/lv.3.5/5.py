# 첫 번째 숫자가 가장 큰지 검사

# 숫자 3개를 입력 받아라
# 이중 첫번째로 입력받은 숫자가 나머지 숫자 2개보다 같거나 큰 숫자인지 알려주는 프로그램을 작성해라

# 3 5 1이 입력되면 max발견



num = list(map(int, input().split()))

max = num[0]
cnt = 0
for i in range(len(num)):
    if max <= num[i]:
        cnt += 1


if cnt > 0:
    print('MAX아님')
else:
    print('MAX발견')