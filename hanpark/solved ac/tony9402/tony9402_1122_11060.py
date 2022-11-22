# tony9402 11060 점프 점프

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().strip().split()))
ls = [21e8]*(N+1)
ls[0] = 0
for n in range(N):
    for m in range(lst[n]):
        if n + m < N:
            ls[n+m+1] = min(ls[n+m+1], ls[n]+1)
if ls[N-1] < 21e8:
    print(ls[N-1])
else:
    print(-1)