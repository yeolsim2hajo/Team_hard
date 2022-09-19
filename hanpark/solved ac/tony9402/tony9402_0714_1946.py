# 백준 1946 신입 사원

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort()
    rst, ans = arr[0][1], 1
    for i in range(n):
        m = arr[i][1]
        if rst > m:
            rst = m
            ans += 1
    print(ans)