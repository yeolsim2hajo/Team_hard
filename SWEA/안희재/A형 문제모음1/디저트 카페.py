# Dfs인가 bfs인가. -> 최소로 가는게 아니라, 그 좌표에서 가능한 모든 사각형이니까 DFS인듯
# 너무 많이 탐색하는 것 같은데.. 
    # 결국 디버깅도 실패 -> 다른 방법으로 가자..
import sys
sys.stdin = open('desert_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]


    def dfs(x,y):
        global path, Max, ex, ey
        if x == ex and y == ey and len(path) > 3: # 처음에 바로 돌아오는경우 컷!
            if Max < len(path):
                Max = len(path)
                return
        if x == ex and y == ey and len(path) == 3:
            return
        
        for dx,dy in [(-1,-1), (-1,1), (1,-1), (1,1)]: # 11,1,7,5시
            nx, ny = x+dx, y+dy
            if not(0<=nx<N and 0<=ny<N): continue 
            if nx == ex and ny == ey:
                visit[nx][ny] = 1 
                path.append(arr[nx][ny])
                tmp = len(path)-1
                dfs(nx,ny)
                path = path[0:tmp] # 원상복구
                visit[nx][ny] = 0
            else:
                if visit[nx][ny] == 1: continue 
                if arr[nx][ny] in path: continue # 이전에 먹어본 종류면 컷
                visit[nx][ny] = 1 
                path.append(arr[nx][ny])
                tmp = len(path)-1
                dfs(nx,ny)
                path = path[0:tmp] # 원상복구
                visit[nx][ny] = 0


    result = 0 # 
    for i in range(0,N-2): # 제일 작은 사각형이 2*2이며, 따라서 (N-3,N-2)가 마지막 좌표
        for j in range(1,N-1): # (0,0과 0,N은 사각형 만들 수 없음)
            path = [arr[i][j]] # 초기값 넣고 시작
            visit = [[0]*N for _ in range(N)] # 처음 시작점은 visit = 1 넣기 ㄴㄴ; 못 돌아감
            Max = 0
            ex,ey = i, j
            dfs(i,j)
            if result < Max:
                result = Max

    if result == 0: # 변화없으면 디저트 순회 못함-> -1!
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {result-1}') # 내 코드에서는 고향 돌아올때 고향도 path에 추가하므로 최종적으로 고향이2개가됨