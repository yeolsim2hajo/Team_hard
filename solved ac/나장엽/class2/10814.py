N = int(input())
data = []
for _ in range(N):
    data.append(list(input().split()))
# 나이 오름차순 정렬, 같으면 등록순으로
data.sort(key = lambda x : int(x[0]))

for i in range(N):
    print(data[i][0], data[i][1])