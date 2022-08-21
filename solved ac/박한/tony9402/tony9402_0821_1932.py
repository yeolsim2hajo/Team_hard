# 백준 1932 정수 삼각형

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
rst = 2
for i in range(1, n):
    for j in range(rst):
        if j == 0:
            arr[i][j] = arr[i][j] + arr[i-1][j]
        elif i == j:
            arr[i][j] = arr[i][j] + arr[i-1][j-1]
        else:
            if arr[i-1][j-1] > arr[i-1][j]:
                arr[i][j] = arr[i][j] + arr[i-1][j-1]
            else:
                arr[i][j] = arr[i][j] + arr[i-1][j]
    rst += 1
print(max(arr[n-1]))