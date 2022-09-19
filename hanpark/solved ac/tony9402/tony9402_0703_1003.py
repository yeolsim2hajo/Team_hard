# 백준 1003 피보나치 함수

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    a, b = 1, 0
    if n!= 0:
        for i in range(n):
            a, b = b, a+b
    print(a, b)