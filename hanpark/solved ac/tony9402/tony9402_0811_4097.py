# 백준 4097 수익

import sys
input = sys.stdin.readline
while 1:
    n = int(input())
    if n == 0:
        break
    lst = [int(input()) for _ in range(n)]
    for i in range(n-1):
        if lst[i] > 0:
            lst[i+1] += lst[i]
    print(max(lst))