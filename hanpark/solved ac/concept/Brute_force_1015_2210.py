# 백준 2210 숫자판 점프

import sys
input = sys.stdin.readline

arr = [list(input().strip().split()) for _ in range(5)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
lst = []
def bf(a, b, c):
    c += arr[a][b]
    if len(c) == 6:
        if c not in lst:
            lst.append(c)
        return
    for n in range(4):
        ny = a + dy[n]
        nx = b + dx[n]
        if 0 <= ny < 5 and 0 <= nx < 5:
            bf(ny, nx, c)
for i in range(5):
    for j in range(5):
        bf(i, j, '')
print(len(lst))

# 많이 활용해본 방식 - dy, dx를 활용