# 백준 13549 숨바꼭질 3

import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
lst = [-1 for _ in range(100001)]
lst[N] = 0
q = deque()
q.append(N)
while q:
    n = q.popleft()
    if n == K:
        print(lst[n])
        break
    if 0 <= n-1 < 100001 and lst[n-1] == -1:
        lst[n-1] = lst[n]+1
        q.append(n-1)
    if 0 < n*2 < 100001 and lst[n*2] == -1:
        lst[n*2] = lst[n]
        q.appendleft(n*2)
    if 0 <= n+1 < 100001 and lst[n+1] == -1:
        lst[n+1] = lst[n]+1
        q.append(n+1)