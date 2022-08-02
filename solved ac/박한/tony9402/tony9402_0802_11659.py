# 백준 11659 구간 합 구하기 4

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))
arr = [0]*(n+1)
for i in range(n):
    arr[i+1] = arr[i] + lst[i]
for _ in range(m):
    s, e = map(int, input().split())
    print(arr[e]-arr[s-1])