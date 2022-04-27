# direct는 오른쪽 / 아래만 -> 따라서, 재방문 경우는 고려 안해도됨(아래로 갔다가 왼쪽으로? 불가)
# (0,0)에서 (N-1,N-1) 도달하면 종료(return)

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # N*n
    arr = [list(map(int,input().split())) for _ in range(N)]

    Min = 2e18
    def dfs(x,y,Sum): # x,y는 좌표
        global Min
        if x == N-1 and y == N-1:
            if Sum < Min:
                Min = Sum
            return

        directx = [1,0]
        directy = [0,1]
        for i in range(2):
            dx = x+directx[i]
            dy = y+directy[i]
            if not(0<=dx<=N-1 and 0<=dy<=N-1): continue # 배열 범위 벗어나면 컷
            dfs(dx,dy,Sum+arr[dx][dy])
            
    dfs(0,0,arr[0][0]) # Sum의 초기값은 시작위치 고정!
    print(f'#{tc} {Min}')