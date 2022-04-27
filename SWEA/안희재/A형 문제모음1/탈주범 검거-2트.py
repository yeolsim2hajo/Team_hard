# 와 pipe랑 opp로 연결가능여부를 체크해줬네 개쩐다;;
# 또한, Opp는 정말 많이 쓰이는 기법!
import sys
from collections import deque

sys.stdin = open('escape_input.txt','r')

def bfs(x,y,level):
    global cnt
    q = deque()
    q.append((x,y,level))
    # 0번인덱스는 더미(1번인덱스에 1번파이프 정보 놓기 위해)
    # [상,하,좌,우] 정보
    pipe = [[0,0,0,0],[1,1,1,1],[1,1,0,0],[0,0,1,1],[1,0,0,1],[0,1,0,1],[0,1,1,0],[1,0,1,0]]
    Opp = [1,0,3,2]

    while q:
        nowx,nowy,level = q.popleft()
        if level == L: return

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for k in range(4): # 상,하,좌,우
            nx,ny = nowx+dx[k],nowy+dy[k]
            if not(0<=nx<N and 0<=ny<M): continue
            if arr[nx][ny] == 0: continue
            if visit[nx][ny] == 1: continue
            if pipe[arr[nowx][nowy]][k] == 1 and pipe[arr[nx][ny]][Opp[k]] == 1:
                visit[nx][ny] = 1
                q.append((nx,ny,level+1))
                cnt += 1

T = int(input())
for tc in range(1,T+1):
    N, M, R, C, L = map(int,input().split()) # N은 행,M은 열, (R,C)는 시작점(맨홀), L은 level인셈(제한시간)
    arr = [list(map(int,input().split())) for _ in range(N)]
    visit = [[0]*M for _ in range(N)]
    visit[R][C] = 1
    cnt = 1 # 처음 맨홀위치는 세고 시작
    bfs(R,C,1) # 탈주범 맨홀에서 다른칸가려면 총 2시간 소요니까 -> 1이 초기값 

    print(f'#{tc}', cnt)