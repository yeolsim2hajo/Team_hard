# 백준 class 3++ 1389 케빈 베이컨의 6단계 법칙

from collections import deque

n, m = map(int, input().split())
arr = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1

rst, ans, tar = 0, 21e8, 0

def bfs(loc):
    global rst
    check, lst = [0]*n, [0]*n
    check[loc] = 1
    q = deque([loc])
    while q:
        nowloc = q.popleft()
        for i in range(n):
            if arr[nowloc][i] == 1 and check[i] == 0:
                check[i] = 1
                lst[i] = lst[nowloc] + 1
                q.append(i)
    rst = sum(lst)

for i in range(n):
    bfs(i)
    if ans > rst:
        ans = rst
        tar = i+1

print(tar)