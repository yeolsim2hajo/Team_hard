# 백준 17390 이건 꼭 풀어야 해!

import sys
input = sys.stdin.readline
n, q = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
lst1 = [0]*(n+1)
for i in range(n):
    lst1[i+1] = lst1[i] + lst[i]
for _ in range(q):
    a, b = map(int, input().split())
    ans = lst1[b]-lst1[a-1]
    print(ans)