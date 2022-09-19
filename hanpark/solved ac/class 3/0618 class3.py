# 백준 class 3++ 1260 DFS와 BFS

from collections import deque

n, m, v = map(int, input().split())
arr = [[0]*n for _ in range(n)]
checkD, checkB = [0]*n, [0]*n
for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1
lstD, lstB = [], []

def dfs(level):
    for i in range(n):
        if arr[level][i] == 1 and checkD[i] == 0:
            checkD[i] = 1
            lstD.append(i+1)
            dfs(i)

def bfs(loc):
    q = deque([loc])
    while q:
        nowloc = q.popleft()
        for i in range(n):
            if arr[nowloc][i] == 1 and checkB[i] == 0:
                checkB[i] = 1
                lstB.append(i+1)
                q.append(i)

checkD[v-1] = 1
lstD.append(v)
dfs(v-1)
print(*lstD)
checkB[v-1] = 1
lstB.append(v)
bfs(v-1)
print(*lstB)