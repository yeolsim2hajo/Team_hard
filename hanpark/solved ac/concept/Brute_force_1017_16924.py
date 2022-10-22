# 백준 16924 십자가 찾기

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().strip().split())
arr = [list(input().strip()) for _ in range(N)]
ls = [[0 for _ in range(M)] for _ in range(N)]
lst = []
rst = 0

def bfs(y, x):
    global lst
    q = deque()
    directy, directx = [0, 1, 0, -1], [1, 0, -1, 0]
    for d in range(4):
        dy,dx = y+directy[d], x+directx[d]
        if dy >= 0 and dy < N and dx >= 0 and dx < M and arr[dy][dx] == '*':
            q.append([dy, dx, d])
        if len(q) == 4:
            ls[y][x] = 1
    check = 1
    while(len(q) == 4):
        lst.append(str(y+1) + " " + str(x+1) + " " + str(check))
        for a in range(4):
            b = q.popleft()
            ls[b[0]][b[1]] = 1
            ay, ax = b[0] + directy[b[2]], b[1] + directx[b[2]]
            if ay >= 0 and ay < N and ax >= 0 and ax < M and arr[ay][ax] == '*':
                q.append([ay, ax, a])
        check += 1

for i in range(N):
    for j in range(M):
        if arr[i][j] == '*':
            rst += 1
            bfs(i, j)
lsum = 0
for i in range(N):
    lsum += sum(ls[i])
if len(lst) == 0 or rst != lsum:
    print(-1)
else:
    print(len(lst))
    for l in lst:
        print(l)

# arr 순회하면서 "*" 찾기
# bfs 통해 네 방향 값이 "*"일 경우 q에 좌표와 길이정보를 저장하기
# q 길이가 4가 되면 lst에 값 추가하기
# 그 후 십자가를 체크한 ls 항목의 '1' 개수와 전체 "*" 개수가 동일한지를 체크
# lst의 개수가 0인지도 체크해서 둘 다 불만족할 경우 -1 출력, 정상적이면 십자가 정보 출력