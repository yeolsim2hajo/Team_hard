# 흠, 거꾸로 올라올까? 맨 아래에서 2 찾은 다음, 거꾸로 올라와서 0행의 y좌표를 찾는 거지
# 또한, 첫 줄에서 1이 있는 y좌표만 골라서 direct에 만들어줌
    # 현 위치는 값이 2인 y좌표
# 아래에서 올라올 때, 좌에 1이 있으면 현 위치에서 -1(direct에서) / 우에 1이 있으면 +1
# --------------------------------------------------------------------
# 2트 - 성공!
for tc in range(1,11):
    num = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    start = [] # 사다리 시작 지점들(0행 j열들)의 y좌표를 start에 담는다
    for j in range(100):
        if arr[0][j] == 1:
            start.append(j)

    now_x = 99 # 처음에 이건 무조건 99, x좌표(행)
    now_y = 0 # 맨 아랫줄에서, 값이 2인 y좌표 탐색
    for j in range(100):
        if arr[99][j] == 2:
            now_y = j

    now_index = 0 # start = [0,4,7,9]고, 2가 있는 y좌표가 9라면 now_index는 3
    for i in range(len(start)):
        if now_y == start[i]:
            now_index = i

    while now_x > -1:
        if now_y-1>= 0 and arr[now_x][now_y-1] == 1: # 좌가 1이라면
            now_index -= 1
            now_y = start[now_index]
            now_x -= 1
        elif now_y+1 < 100 and arr[now_x][now_y+1] == 1: # 우가 1이라면
            now_index += 1
            now_y = start[now_index]
            now_x -= 1
        else: # 좌우가 다 0이라면, 그냥 올라가기만
            now_x -= 1

    print(f'#{num}', start[now_index])
# --------------------------------------------------------------------