import copy
N, W, H = map(int,input().split()) # H가 행, W가 열임.. / N은 쏘는 구슬 개수
arr = [list(map(int,input().split())) for _ in range(H)]

# 터지는 범위에, 2이상의 숫자가 있으면 거기에도 영향 줌
    # 다행인건, 연쇄 폭발이 일어날 때에는, 한꺼번에 벽돌이 처리된다는 것 -> 즉, gravity가 작동하지 않음
    # bomb는 무조건 bfs로. -> 만약, 터지는 범위에 2이상 있으면 그것도 stack에 넣기
def bomb(x,y): 
    q = [(x,y)] # q에 초기값 넣기
    dx,dy = [-1,1,0,0],[0,0,-1,1] # 상하좌우

    while q:
        nowx,nowy = q.pop(0)
        tmp = arr[nowx][nowy]
        arr[nowx][nowy] = 0 # 자기자신은 일단 먼저 파괴
        if tmp >= 2: # 2이상이면
            for k in range(1,tmp): # 2면 주위는 1번만
                for i in range(4):
                    nx = nowx+dx[i]*k
                    ny = nowy+dy[i]*k
                    if not(0<=nx<H and 0<=ny<W): continue
                    if arr[nx][ny] >= 2:
                        q.append((nx,ny))
                    else: # 1짜리는 폭탄범위내에 있으면 다 파괴
                        arr[nx][ny] = 0

def gravity():
    for i in range(W):
        start = -1
        while 1:
            if arr[start][i] != 0:
                start -= 1
                if abs(start) == H+1:
                    break
            else: # 0이면, 이제 여기에다 위의 0아닌 벽돌들을 떨어트릴 것. 여기가 시작점임. 그 아래는 이미 채워져있으니 중력ㄴㄴ
                break
        if abs(start) == H+1:
            continue
        else:
            now,space = start, start
            while 1:
                if arr[now][i] == 0:
                    now -= 1
                else:
                    arr[now][i],arr[space][i] = arr[space][i],arr[now][i]
                    space -= 1
                if abs(now) == H+1:
                    break

def dfs(level):
    global Min, arr
    if level == N:
        cnt = 0
        for i in range(H):
            for j in range(W):
                if arr[i][j] >= 1:
                    cnt += 1
        if Min > cnt: # 남아있는 갯수가 제일 적다는 것은, 그만큼 많이 부신 것
            Min = cnt
        return

    branch = []
    for i in range(W):
        for j in range(H):
            if arr[j][i] >= 1:
                branch.append((j,i))
                break

    if len(branch) == 0:
        dfs(level+1)
    else:
        tmp = copy.deepcopy(arr)
        for bx,by in branch:
            bomb(bx,by)
            gravity()
            dfs(level+1)
            arr = copy.deepcopy(tmp)

Min = 2e18
dfs(0)
print(Min)