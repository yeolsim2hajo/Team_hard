# 백준 2160 그림 비교

import sys
input = sys.stdin.readline
n = int(input())
arr, minn = [], 21e8
a, b = 0, 0
for n in range(n):
    lst = [input().strip() for _ in range(5)]
    arr.append(lst)
for i in range(n-1):
    for j in range(i+1, n):
        rst = 0
        for o in range(5):
            for p in range(7):
                if arr[i][o][p] != arr[j][o][p]:
                    rst += 1
        if rst < minn:
            minn = rst
            a = i
            b = j
print(f"{a+1} {b+1}")