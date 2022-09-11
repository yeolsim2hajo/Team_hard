import sys
input = sys.stdin.readline

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

memo = [[-1] * n for _ in range(n)]


# dfs로 탐색하기  0, 0 부터 시작
def dfs(x, y):
    global memo

    if x == n - 1 and y == n - 1:
        return 1

    if memo[x][y] == -1 :
        memo[x][y] = 0
        if 0 <= x + graph[x][y] < n:
            memo[x][y] += dfs(x + graph[x][y], y)
            
        if 0 <= y + graph[x][y] < n:
            memo[x][y] += dfs(x, y + graph[x][y])

    return memo[x][y]

print(dfs(0, 0))