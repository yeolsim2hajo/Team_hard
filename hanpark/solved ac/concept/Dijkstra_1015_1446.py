# 백준 1446 지름길

import sys
input = sys.stdin.readline
from collections import deque

q = deque()
n, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:x[0])
for i in range(n):
    q.append(arr[i])
rst = 21e8
check = [rst for _ in range(d+1)]
check[0] = 0
for i in range(d):
    while q and q[0][0] == i:
        ans = q.popleft()
        if ans[1] > d:
            continue
        if check[ans[1]] > check[i]+ans[2]:
            check[ans[1]] = check[i]+ans[2]
        else:
            check[ans[1]] = check[ans[1]]
    if check[i+1] > check[i]+1:
        check[i+1] = check[i]+1
print(check[d])