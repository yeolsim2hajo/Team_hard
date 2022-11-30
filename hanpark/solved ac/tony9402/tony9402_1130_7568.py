# 백준 7568 덩치

import sys
input = sys.stdin.readline

N = int(input())
lst = [input.split() for _ in range(N)]
for i in range(N):
    ans = 1
    for j in range(N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            ans = ans + 1
    print(ans ,end=" ")