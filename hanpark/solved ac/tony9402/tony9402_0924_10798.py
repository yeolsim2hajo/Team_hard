# 백준 10798 세로읽기

import sys
input = sys.stdin.readline

arr, n = [['']*15 for _ in range(5)], 0
for i in range(5):
    lst = list(input().strip())
    for j in range(len(lst)):
        arr[i][j] = lst[j]
    if len(lst) > n:
        n = len(lst)
for a in range(n):
    for b in range(5):
        if arr[b][a] != '':
            print(arr[b][a], end="")