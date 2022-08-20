# 백준 16927 배열 돌리기 2

import sys
input = sys.stdin.readline
from collections import deque

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
def rotate_arr(r):
    global N, M, arr
    q = deque()
    _width, _height = M, N
    time = min(_width, _height) // 2
    nx, ny = 0, 0
    while time >= 1:
        for i in range(_width-1):
            q.append(arr[ny][nx+i])
        for i in range(_height-1):
            q.append(arr[ny+i][nx+_width-1])
        for i in range(_width-1):
            q.append(arr[ny+_height-1][nx+_width-1-i])
        for i in range(_height-1):
            q.append(arr[ny+_height-1-i][nx])
        q.rotate(-r)
        for i in range(_width-1):
            arr[ny][nx+i] = q.popleft()
        for i in range(_height-1):
            arr[ny+i][nx+_width-1] = q.popleft()
        for i in range(_width-1):
            arr[ny+_height-1][nx+_width-1-i] = q.popleft()
        for i in range(_height-1):
            arr[ny+_height-1-i][nx] = q.popleft()
        _width -= 2
        _height -= 2
        nx += 1
        ny += 1
        time = min(_width, _height) // 2
rotate_arr(r)
for i in range(n):
    print(*arr[i])