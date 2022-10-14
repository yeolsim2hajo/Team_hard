# 백준 14496 그대, 그머가 되어

import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())
N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
lst = [0]*(N+1)
for _ in range(M):
    x, y = map(int, input().split())
    if x != y:
        arr[x].append(y)
        arr[y].append(x)
def abc():
    q = deque([(a, 0)])
    lst[a] = 1
    while q:
        i, j = q.popleft()
        if i == b:
            print(j)
            return
        for n in arr[i]:
            if lst[n] == 0:
                lst[n] = 1
                q.append((n, j+1))
    print(-1)
abc()