# 완전탐색, N<=50 이하, 단순 for문으로 해결 가능
# https://www.acmicpc.net/problem/7568

N = int(input())
data = []
answer = []
for i in range(N):
    weight, height = map(int, input().split())
    data.append((weight, height))

for i in range(N):
    rank = 0 # 등수 
    count = 0 # 몸무게와 키가 큰 사람을 세는 변수
    for k in range(N):
        if data[i][0] < data[k][0] and data[i][1] < data[k][1]: # 자신보다 몸무게, 키가 큰 사람이면?
            count += 1 # 사람의 수 += 1
    rank = count 
    answer.append(rank + 1) # 덩치는 자신보다 큰 사람의 수 + 1

for i in answer:
    print(i, end = ' ')