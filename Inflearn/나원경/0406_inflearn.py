#70 행렬 곱하기
a = ([1,2],[2,4])
b = ([1,0],[0,3])
a_n = len(a)
a_m = len(a[0])
if a_n == len(b[0]) and a_m == len(b):
    result = [[0]*a_n for _ in range(a_n)]
    for i in range(a_n):
        for j in range(a_n):
            for k in range(a_m):
                result[i][j] += a[i][k]*b[k][j]
    print(tuple(result))
else:
    print(-1)


#74 최장 경로 찾기
def dfs(arg,cnt=0):
    global max_path
    for num in graph[arg]:
        if visited[num] == 0:
            visited[num] = 1
            dfs(num,cnt+1)
            if cnt > max_path:
                max_path = cnt
            visited[num] = 0

graph = {1: [2,3,4],
         2: [1,3,4,5,6],
         3: [1,2,7],
         4: [1,2,5,6],
         5: [2,4,6,7],
         6: [2,4,5,7],
         7: [3,5,6]}
max_path = 0
start, end = 1, 7
visited = [0]*8
dfs(start)
print(max_path)
