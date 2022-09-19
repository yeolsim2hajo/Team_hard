# 백준 2167 2차원 배열의 합

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr1 = [[0]*(M+1) for _ in range(N+1)]
for n in range(1, N+1):
    for m in range(1, M+1):
        arr1[n][m] = (arr[n-1][m-1] + arr1[n][m-1] + arr1[n-1][m]) - arr1[n-1][m-1]
K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    print((arr1[x][y]+arr1[i-1][j-1])-(arr1[x][j-1] + arr1[i-1][y]))