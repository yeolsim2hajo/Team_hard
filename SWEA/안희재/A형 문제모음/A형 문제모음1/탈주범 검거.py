# 새 배열에 flood fill로 채우고, L이하인 것만 cnt
    # 0인 곳은 못감(1이상인 곳만 이동할 여.지가 있음)
    # 1 -> 상하좌우 / 2 -> 상하
    # 3 -> 좌우 / 4 -> 좌우
    # 5 -> 하우 / 6 -> 하좌 / 7 -> 상좌
    # 아 추가로 다음 위치가 이전위치랑 연결될 수 있는지도 확인해야함 - > 이게 point
        # 즉, 재방문 + arr[nx][ny] ==0 이외에도 위 조건 더 추가해야!
        # 음.. 인접칸에 파이프가 있지만, 끊긴 파이프라는 것을 어떻게 표현하지?
        # 특히, 3,4의 경우: 3의 왼쪽에서는 4와 연결가능하지만 3의 오른쪽에선 불가능 ㅠㅠㅠ
        # 쉬운게 아니네;;

# 노가다 코드 -> 꺼져!
import sys
from collections import deque

sys.stdin = open('escape_input.txt','r')

def bfs(x,y,level):
    q = deque()
    q.append((x,y,level))

    while q:
        nowx,nowy,level = q.popleft()
        if level > L: return # 제한시간 초과하면 컷

        if arr[nowx][nowy] == 1:
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = nowx+dx, nowy+dy
                if not(0<=nx<N and 0<=ny<M): continue
                if visit[nx][ny] >= 1 or arr[nx][ny] == 0: continue
                visit[nx][ny] = level+1
                q.append((nx,ny,level+1))
        elif arr[nowx][nowy] == 2:
            for dx, dy in [(-1,0),(1,0)]:
                nx, ny = nowx+dx, nowy+dy
                if not(0<=nx<N and 0<=ny<M): continue
                if visit[nx][ny] >= 1 or arr[nx][ny] == 0: continue
                if (dx,dy) == (-1,0) and (arr[nx][ny] == 3 or arr[nx][ny] == 4 or arr[nx][ny] == 7): continue
                if (dx,dy) == (1,0) and (arr[nx][ny] == 3 or arr[nx][ny] == 5 or arr[nx][ny] == 6): continue
                visit[nx][ny] = level+1
                q.append((nx,ny,level+1))
        elif arr[nowx][nowy] == 3:
            for dx, dy in [(0,-1),(0,1)]:
                nx, ny = nowx+dx, nowy+dy
                if not(0<=nx<N and 0<=ny<M): continue
                if visit[nx][ny] >= 1 or arr[nx][ny] == 0: continue
                if (dx,dy) == (0,-1) and (arr[nx][ny] ==2 or arr[nx][ny] == 6 or arr[nx][ny] == 7): continue
                if (dx,dy) == (0,1) and (arr[nx][ny] == 2 or arr[nx][ny] == 4 or arr[nx][ny] == 5): continue
                visit[nx][ny] = level+1
                q.append((nx,ny,level+1))
        elif arr[nowx][nowy] == 4:
            for dx, dy in [(-1,0),(0,1)]:
                nx, ny = nowx+dx, nowy+dy
                if not(0<=nx<N and 0<=ny<M): continue
                if visit[nx][ny] >= 1 or arr[nx][ny] == 0: continue
                if (dx,dy) == (-1,0) and (arr[nx][ny] == 3 or arr[nx][ny] == 7): continue
                if (dx,dy) == (0,1) and (arr[nx][ny] == 2 or arr[nx][ny] == 5): continue
                visit[nx][ny] = level+1
                q.append((nx,ny,level+1))
        elif arr[nowx][nowy] == 5:
            for dx, dy in [(1,0),(0,1)]:
                nx, ny = nowx+dx, nowy+dy
                if not(0<=nx<N and 0<=ny<M): continue
                if visit[nx][ny] >= 1 or arr[nx][ny] == 0: continue
                if (dx,dy) == (1,0) and (arr[nx][ny] == 3 or arr[nx][ny] == 6): continue
                if (dx,dy) == (0,1) and (arr[nx][ny] == 2 or arr[nx][ny] == 4): continue
                visit[nx][ny] = level+1
                q.append((nx,ny,level+1))
        elif arr[nowx][nowy] == 6:
            for dx, dy in [(1,0),(0,-1)]:
                nx, ny = nowx+dx, nowy+dy
                if not(0<=nx<N and 0<=ny<M): continue
                if visit[nx][ny] >= 1 or arr[nx][ny] == 0: continue
                if (dx,dy) == (1,0) and (arr[nx][ny] == 3 or arr[nx][ny] == 5): continue
                if (dx,dy) == (0,-1) and (arr[nx][ny] == 2 or arr[nx][ny] == 7): continue
                visit[nx][ny] = level+1
                q.append((nx,ny,level+1))
        elif arr[nowx][nowy] == 7:
            for dx, dy in [(-1,0),(0,-1)]:
                nx, ny = nowx+dx, nowy+dy
                if not(0<=nx<N and 0<=ny<M): continue
                if visit[nx][ny] >= 1 or arr[nx][ny] == 0: continue
                if (dx,dy) == (-1,0) and (arr[nx][ny] == 3 or arr[nx][ny] == 4): continue
                if (dx,dy) == (0,-1) and (arr[nx][ny] == 2 or arr[nx][ny] == 6): continue
                visit[nx][ny] = level+1
                q.append((nx,ny,level+1))


T = int(input())
for tc in range(1,T+1):
    N, M, R, C, L = map(int,input().split()) # N은 행,M은 열, (R,C)는 시작점(맨홀), L은 level인셈(제한시간)
    arr = [list(map(int,input().split())) for _ in range(N)]
    visit = [[0]*M for _ in range(N)]
    visit[R][C] = 1
    bfs(R,C,1) # 탈주범 맨홀에서 다른칸가려면 총 2시간 소요니까 -> 1이 초기값 
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visit[i][j] > 0:
                cnt += 1
    print(f'{tc}', cnt)

