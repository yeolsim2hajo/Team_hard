# 백준 14697 방 배정하기

import sys
input = sys.stdin.readline

A, B, C, N = map(int, input().split())
rst = 0
for a in range(101):
    for b in range(101):
        for c in range(101):
            if a*A + b*B + c*C == N:
                rst = 1
                break
print(rst)