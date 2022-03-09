arr = [['_']*5 for _ in range(4)]

dx = [-1,-1,-1,0,0,1,1,1] # 행, 11시 시작해서 일렬로 쭈욱 그다음 행 일렬 쭈욱
dy = [-1,0,1,-1,1,-1,0,1] # 열

def sum(x, y):
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < 4 and 0 <= ny < 5:
            arr[nx][ny] = '#'

for i in range(2):
    bomb = list(map(int,input().split()))
    sum(bomb[0], bomb[1])

for i in range(4):
    print(*arr[i])
