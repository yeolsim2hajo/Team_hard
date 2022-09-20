N, M = map(int,input().split()) # N은 행, M은 열
r, c, d = map(int,input().split()) 
arr = [list(map(int,input().split())) for _ in range(N)] # 0 : 빈칸, 1: 벽
cnt = 1 # 청소한 칸의 수 - 등장칸 청소하고 시작하니, 1부터
arr[r][c] = 2 # 청소하면 2로 바꾸고, 등장칸은 일단 청소하고 보는 거지


# d는 바라보는 방향이며, 0(북), 1(동), 2(남), 3(서)
x, y = r, c # x, y는 현재 위치(계속 갱신시킬 것임)

while (1):
    stack = [x,y]
    # 0.현재 위치에서 바라보는 방향 기준으로, 왼쪽방 탐색으로 시작
    if d == 0:
        if arr[x][y-1] == 0: # 북방향의 왼쪽인 서쪽이 청소해야 한다면,
            x, y, d = x, y-1, 3 # 좌표 이동하고, 방향은 서쪽(3)으로 바꿈
            arr[x][y] = 2
            cnt += 1
        else: # 벽이거나, 이미 청소했다면 방향만 회전하고 다시 ㄱㄱ
            d = 3
    elif d == 3:
        if arr[x+1][y] == 0: # 서쪽의 왼쪽인 남쪽
            x, y, d = x+1, y, 2
            arr[x][y] = 2
            cnt += 1
        else:
            d = 2
    elif d == 2:
        if arr[x][y+1] == 0:
            x, y, d = x, y+1, 1
            arr[x][y] = 2
            cnt += 1
        else:
            d = 1
    else: # d == 1
        if arr[x-1][y] == 0:
            x, y, d = x-1, y, 0
            arr[x][y] = 2
            cnt += 1
        else:
            d = 0

    if stack == [x,y]: # stack(이전)이랑 현재 x,y가 같다면 : x,y가 안바뀌었다는 뜻
        # 사방이 모두 0이 아니라면, 후진 코드 넣고 -> 후진도 안되면 break
        if arr[x-1][y] != 0 and arr[x][y-1] != 0 and arr[x+1][y] != 0 and arr[x][y+1] != 0:
            if d == 0:
                x, y = x+1, y
                if arr[x][y] == 1:
                    break
            elif d == 1:
                x, y = x, y-1
                if arr[x][y] == 1:
                    break
            elif d == 2:
                x, y = x-1, y
                if arr[x][y] == 1:
                    break
            else:
                x, y = x, y+1
                if arr[x][y] == 1:
                    break

print(cnt)
    
# 아니 후진조건을 내가 아예 이해를 못한 것 같음
# 후진의 경우, 네 방향을 다.시 모두 살핀 후에 네방향이 모두 0이 아니면,
# 그때서야 후진하는데 그.때 바라보고 있.던 방향이 어디인가?
# 또한, 계속 죽죽 후진하는게 아니라 한칸 후진하고 또4방향 살피고 이런식?
# 아 ㅅㅂ 존나 어지럽네
# 이렇게 길게 하는게 아닌것 같은데..
# 다시 ㄱ 이거 아님. 