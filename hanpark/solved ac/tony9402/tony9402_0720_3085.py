# 백준 3085 사탕게임

# 디버깅 못하겟음..

import sys
input = sys.stdin.readline
n = int(input())
rst = 0
arr = [list(input().strip()) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n-1):
        if arr[i][j] != arr[i][j+1]:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            for a in range(n):
                rst = 1
                for b in range(n-1):
                    if arr[a][b] == arr[a][b+1]:
                        rst += 1
                        if rst > ans:
                            ans = rst
                    else:
                        rst = 1
            for a in range(n):
                rst = 1
                for b in range(n-1):
                    if arr[b][a] == arr[b+1][a]:
                        rst += 1
                        if rst > ans:
                            ans = rst
                        else:
                            rst = 1
            arr[i][j+1], arr[i][j] = arr[i][j], arr[i][j+1]
        if arr[j][i] != arr[j+1][i]:
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
            for a in range(n):
                rst = 1
                for b in range(n-1):
                    if arr[a][b] == arr[a][b+1]:
                        rst += 1
                        if rst > ans:
                            ans = rst
                    else:
                        rst = 1
            for a in range(n):
                rst = 1
                for b in range(n-1):
                    if arr[b][a] == arr[b+1][a]:
                        rst += 1
                        if rst > ans:
                            ans = rst
                        else:
                            rst = 1
            arr[j+1][i], arr[j][i] = arr[j][i], arr[j+1][i]
print(ans)