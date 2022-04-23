#direct를 이용해 flag 주변 4방향에 지뢰를 출력
def mine(y, x):         
    global arr     
    direct_y = [-1,1,0,0]
    direct_x = [0,0,-1,1]

    for i in range(4):
        ny = direct_y[i]+y
        nx = direct_x[i]+x
        if 0 <= ny < 5 and 0 <= nx < 5:
            arr[ny][nx] = '*'

#flag를 찾아 좌표값을 mine함수에 전달
def abc(arr):
    for i in range(len(arr)):
        for k in range(len(arr[i])):
            if arr[i][k] == 1:
                y, x, = i, k
                arr[i][k] = 'f'
                mine(y,x)
#main
arr = [list(map(int, input().split())) for _ in range(5)]
abc(arr)
for i in range(5):
    print(*arr[i], sep= ' ')