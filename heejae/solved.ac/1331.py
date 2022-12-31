from sys import stdin
input = stdin.readline

tour = [input() for _ in range(36)]
board = [[0 for _ in range(6)] for _ in range(6)]
sx, sy = ord(tour[0][0]) - 65, int(tour[0][1]) - 1
board[sx][sy] = 1

flag = True

# 고려 사항 1
if abs(ord(tour[0][0]) - ord(tour[-1][0])) == 2 and abs(int(tour[0][1]) - int(tour[-1][1])) == 1 \
            or abs(ord(tour[0][0]) - ord(tour[-1][0])) == 1 and abs(int(tour[0][1]) - int(tour[-1][1])) == 2:
    for i in range(1, len(tour)):
        nx, ny = ord(tour[i][0]) - 65, int(tour[i][1]) - 1
        # 고려 사항 2
        if abs(nx - sx) == 2 and abs(ny - sy) == 1 or abs(nx - sx) == 1 and abs(ny - sy) == 2:
            board[nx][ny] += 1
            # 고려 사항 3
            if board[nx][ny] != 1:
                flag = False
                break
        else:
            flag = False
            break
        sx, sy = nx, ny
else:
    flag = False

if flag:
    print("Valid")
else:
    print("Invalid")