# 백준 9094 수학적 호기심

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    ans = 0
    for n in range(1, N+1):
        for m in range(n+1, N):
            a, b = n, m
            if (a**2 + b**2 + M)%(a * b) == 0:
                ans += 1
    print(ans)