# 백준 11727 2xn 타일링 2

import sys
input = sys.stdin.readline
n = int(input())
lst = [0]*(n+1)
lst[0], lst[1] = 1, 1
if n < 2:
    print(1)
else:
    for i in range(n-1):
        lst[i+2] = lst[i+1] + lst[i]*2
    print(lst[-1]%10007)