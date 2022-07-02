# 백준 2156 포도주 시식

import sys
input = sys.stdin.readline
n = int(input())
lst = [int(input()) for _ in range(n)]
check = [0]*n
if n == 1:
    check[0] = lst[0]
elif n == 2:
    check[0] = lst[0]
    check[1] = lst[1]+lst[1]
else:
    check[0] = lst[0]
    check[1] = lst[0]+lst[1]
    check[2] = max(check[1], lst[0]+lst[2], lst[1]+lst[2])
    for i in range(3, n):
        check[i] = max(max(lst[i]+lst[i-1]+check[i-3], lst[i]+check[i-2]), check[i-1])
print(check[n-1])