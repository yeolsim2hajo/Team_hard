# class 3++ 1780 종이의 개수

import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
d0, d1, d2 = 0, 0, 0

def abc(a, b, m):
    global d0, d1, d2
    rst = 0
    for i in range(a, a+m):
        for j in range(b, b+m):
            if arr[a][b] != arr[i][j]:
                rst = 1
                break
        if rst == 1:
            break
    if rst == 1:
        m //= 3
        for i in range(3):
            for j in range(3):
                abc(a+(m*i), b+(m*j), m)
    else:
        if arr[a][b] == -1:
            d0 += 1
        elif arr[a][b] == 0:
            d1 += 1
        else:
            d2 += 1

abc(0, 0, n)

print(d0)
print(d1)
print(d2)