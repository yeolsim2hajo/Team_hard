# 백준 17393 다이나믹 롤러

import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
lst = []
for i in range(n):
    a, s, e = i, i+1, n-1
    while s <= e:
        m = (s+e)//2
        if A[i] < B[m]:
            e = m-1
        else:
            s = m+1
            a = m
    lst.append(a-i)
print(*lst)