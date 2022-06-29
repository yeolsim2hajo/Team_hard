a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)


# 최소값을 만들기 위해서 -를 기준으로 갈호를 치기..
# 입력을 받을때 - 기준으로 입력을 받아버리고
# 각 원소에 있는 숫자들을 계산해주고
# 맨 처음의 원소는 더해주고 나머지는 빼주기.