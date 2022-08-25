# 백준 1934 최소공배수

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    x, y = a, b
    while x > 0:
        y = y%x
        x, y = y, x
    print(a*b//y)