# 백준 1931 회의실 배정

import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:[x[1], x[0]])

rst, ans = arr[0][1], 1

for i in range(n-1):
    if arr[i+1][0] >= rst:
        ans += 1
        rst = arr[i+1][1]

print(ans)