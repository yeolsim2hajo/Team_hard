# 레퍼런스: path도 인자로 아예 ㄷㄷ;;와우;;;;

import sys
sys.stdin = open('desert_input.txt','r')

def dfs(n,x,y,path):
    global sx, sy, ans
    if n==2 and ans>=len(path)*2: # 이거 넣으면 시간 1/4로 단축됨;;;; 와;;
        return # 딱 절반(이상)왔는데, 그럼에도 정답의 반에도 못미치면.. 어차피 갱신 불가니까 바로 컷!
    if n >3: return
    if n == 3 and (x == sx and y == sy) and ans < len(path):
        ans = len(path)
        return
    
    dx,dy = (1,1,-1,-1,99),(-1,1,1,-1,99) # 마지막은 dummy -> 기술ㄷㄷ;;
    for i in range(n,n+2): # 직진과 시계방향'1'번회전만 허용
        nx,ny = x+dx[i],y+dy[i]
        if not(0<=nx<N and 0<=ny<N): continue
        if arr[nx][ny] in path: continue
        path.append(arr[nx][ny])
        dfs(i,nx,ny,path)
        path.pop()

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = -1
    for sx in range(N-2):
        for sy in range(1,N-1):
            dfs(0,sx,sy,[])

    print(f'#{tc} {ans}')