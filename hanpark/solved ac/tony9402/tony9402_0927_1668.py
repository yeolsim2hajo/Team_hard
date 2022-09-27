# 백준 1668 트로피 진열

import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]
a, b, c, d = 0, 0, 0, 0
for i in range(n):
    if lst[i] > a:
        a = lst[i]
        c += 1
    if lst[n-1-i] > b:
        b = lst[n-1-i]
        d += 1
print(c)
print(d)