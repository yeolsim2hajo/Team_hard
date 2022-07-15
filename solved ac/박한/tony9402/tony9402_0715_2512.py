# 백준 2512 예산

import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
m = int(input())
s, e = 0, max(lst)
while s <= e:
    a = (s+e)//2
    rst = 0
    for i in range(n):
        b = lst[i]
        if b > a:
            rst += a
        else:
            rst += b
    if rst <= m:
        s = a+1
    else:
        e = a-1
print(e)