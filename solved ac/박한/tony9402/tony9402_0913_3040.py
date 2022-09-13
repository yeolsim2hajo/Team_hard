# 백준 3040 백설 공주와 일곱 난쟁이

import sys
input = sys.stdin.readline

lst = [int(input().strip()) for _ in range(9)]
rst = sum(lst)
for i in range(8):
    for j in range(i+1, 9):
        if rst - (lst[i] + lst[j]) == 100:
            lst[i], lst[j] = 0, 0
            for n in range(9):
                if lst[n] > 0:
                    print(lst[n])
            break
    if sum(lst) == 100:
        break