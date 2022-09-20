N = int(input())
graph = [list(input()) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] == 'Y'):
                visited[i][j] = 1

result = 0
for visit in visited:
    result = max(result, sum(visit))
print(result)
출처: https://sangminlog.tistory.com/entry/boj-1058 [로그 남기기:티스토리]