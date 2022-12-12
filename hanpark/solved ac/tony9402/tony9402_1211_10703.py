# 백준 10703 유성

import sys
input = sys.stdin.readline

R, S = map(int, input().split())
lst = [list(input()) for _ in range(R)]
arr = [['.']*S for _ in range(R)]
rst = 3001
for i in range(S):
    a, b = 0, 3001
    flag = False
    for j in range(R):
        if lst[j][i] == 'X':
            if a < j:
                a = j
            flag = True
        if lst[j][i] == '#':
            if b > j:
                b = j
    if flag and rst > b - a - 1:
        rst = b - a - 1
for i in range(R):
    for j in range(S):
        if lst[i][j] == 'X':
            arr[i + rst][j] = 'X'
        elif lst[i][j] == '#':
            arr[i][j] = '#'
for i in range(R):
    for j in range(S):
        print(arr[i][j])
    print()