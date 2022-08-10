# 백준 1080 행렬

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = [list(map(int, input().strip())) for _ in range((n))]
B = [list(map(int, input().strip())) for _ in range((n))]
ans = -1
def abc(y, x):
    for a in range(y, y+3):
        for b in range(x, x+3):
            if B[a][b] == 1:
                B[a][b] = 0
            else:
                B[a][b] = 1
if n < 3 or m < 3:
    if A == B:
        ans = 0
else:
    rst = 0
    for i in range(n-2):
        for j in range(m-2):
            if A[i][j] != B [i][j]:
                rst += 1
                abc(i, j)
    if A == B:
        ans = rst
print(ans)