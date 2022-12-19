# 백준 18232 텔레포트 정거장

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().strip().split())
s, e = map(int, input().strip().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int ,input().strip().split())
    arr[x].append(y)
    arr[y].append(x)
q = deque()
q.append((s, 0))
while q:
    a, b = q.popleft()
    if a == e : 
        print(b)
        break
    for i in [a+1, a-1] :
        if 1<i<n : 
            q.append((i,b+1))
    if arr[a] :
        for i in arr[a] : 
            q.append((i, b+1))