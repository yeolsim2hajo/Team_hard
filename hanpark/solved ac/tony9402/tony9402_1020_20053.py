# 백준 20053 최소, 최대 2

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    print(f"{lst[0]} {lst[-1]}")