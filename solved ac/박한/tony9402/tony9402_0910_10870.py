# 백준 10870 피보나치 수 5

import sys
input = sys.stdin.readline

n = int(input())
a, b = 0, 1
if n < 2:
    print(n)
else:
    for _ in range(n-1):
        b, a = a+b, b
    print(b)