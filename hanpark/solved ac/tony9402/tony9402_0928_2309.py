# 백준 2309 일곱 난쟁이

import sys
input = sys.stdin.readline
lst = [int(input()) for _ in range(9)]
rst, a, b = sum(lst), 0, 0
for i in range(8):
    for j in range(i+1, 9):
        if rst-(lst[i]+lst[j]) == 100:
            a, b = lst[i], lst[j]
            break
lst.sort()
for i in range(9):
    if lst[i] != a and lst[i] != b:
        print(lst[i])