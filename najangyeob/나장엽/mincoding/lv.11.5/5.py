arr = list(map(int, input().split()))


board = [[0]*3 for _ in range(2)]
n = 0
for i in range(2):
    for k in range(3):
        board[i][k] = arr[n]
        n += 1
target = 0
for i in range(2):
    for k in range(3):
        if board[i][k] == target:
            board[i][k] = '#'
        print(board[i][k], end='')
    print()