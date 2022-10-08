#221008
board = [input().split() for _ in range(5)]
numbers = set()

def dfs(row, col, num, level=1):
    if level == 6:
        numbers.add(num)
        return
    for dr, dc in (1,0), (-1,0), (0,1), (0,-1):
        nr, nc = row+dr, col+dc
        if 0 <= nr < 5 and 0 <= nc < 5:
            dfs(nr, nc, num+board[nr][nc], level+1)

for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j])

print(len(numbers))