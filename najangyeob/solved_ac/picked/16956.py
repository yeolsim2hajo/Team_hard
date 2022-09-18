# direct 사용
# 늑대가 양한테 갈 수 있으면 flag = true

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
arr = []

for _ in range(r):
    arr.append(list(input()))
flag = False
for i in range(r):
    for j in range(c):
        if arr[i][j] == "W":
            dy = [-1, 1, 0, 0]
            dx = [0, 0, -1, 1]

            for k in range(4):
                ny = i + dy[k]
                nx = j + dx[k]

                if 0 <= ny < r and 0 <= nx < c and arr[ny][nx] == "S":
                    flag = True
                    break
        elif arr[i][j] == "S":
            continue
        elif arr[i][j] == ".":
            arr[i][j] = "D"

if flag == True:
    print(0)
else:
    print(1)
    for i in arr:
        print(''.join(i))