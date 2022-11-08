# 백준 9094 수학적 호기심

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().strip().split())
    ans = 0
    for a in range(n):
        for b in range(a+1, n-1):
            c, d = a+1, b+1
            if (c**2+d**2+m)%(c*d) == 0:
                ans += 1
    print(ans)