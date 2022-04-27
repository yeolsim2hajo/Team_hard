# 딱봐도 bfs 플러드필이네
# 찾은 미생물은 0으로 박멸시키기
from collections import deque

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split()) # N은 세로(행), M은 가로(열)
    arr = [list(input()) for _ in range(N)]
    # visited = [[0]*M for _ in range(N)]

    def bfs_A(x,y,level):
        global tmp1
        q = deque()
        q.append((x,y,level))

        while q:
            nowx,nowy,level = q.popleft()

            directx = [-1,1,0,0]
            directy = [0,0,-1,1]
            for i in range(4):
                dx = nowx+directx[i]
                dy = nowy+directy[i]
                if not(0<=dx<N and 0<=dy<M): continue
                if arr[dx][dy] != 'A': continue
                arr[dx][dy] = '_' # 찾았으면 박멸(재방문 방지)
                tmp1 += 1
                q.append((dx,dy,level+1))

    def bfs_B(x,y,level):
        global tmp2
        q = deque()
        q.append((x,y,level))

        while q:
            nowx,nowy,level = q.popleft()

            directx = [-1,1,0,0]
            directy = [0,0,-1,1]
            for i in range(4):
                dx = nowx+directx[i]
                dy = nowy+directy[i]
                if not(0<=dx<N and 0<=dy<M): continue
                if arr[dx][dy] != 'B': continue
                tmp2 += 1
                arr[dx][dy] = '_' # 찾았으면 박멸(재방문 방지)
                q.append((dx,dy,level+1))

    a_count, b_count, Max = 0, 0, 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'A':
                tmp1 = 1
                arr[i][j] = '_' # 본인 침몰
                bfs_A(i,j,1)
                if Max < tmp1:
                    Max = tmp1
                a_count += 1 # bfs_A가 돌아갔다면, 일단 A미생물군집 발견한거니 +1

            if arr[i][j] == 'B':
                tmp2 = 1
                arr[i][j] = '_' # 본인 침몰
                bfs_B(i,j,1)
                if Max < tmp2:
                    Max = tmp2
                b_count += 1 # bfs_A가 돌아갔다면, 일단 A미생물군집 발견한거니 +1

    print(f'#{tc}', a_count, b_count, Max)

