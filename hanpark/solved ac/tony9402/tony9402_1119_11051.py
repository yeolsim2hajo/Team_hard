# 백준 11051 이항 계수 2

import sys
N, K = map(int, sys.stdin.readline().split())
lst = []

for i in range(N+1) :
    lst.append([1]*(i+1))

for i in range(2, N+1) :
    for j in range(1, i) :
        lst[i][j]=(lst[i-1][j-1]+lst[i-1][j])%10007

print(lst[N][K])