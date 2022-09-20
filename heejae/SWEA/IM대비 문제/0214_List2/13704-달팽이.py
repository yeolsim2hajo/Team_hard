T = int(input())

for i in range(1,T+1):
    N = int(input()) # N*N 행렬
    arr = [[0]* N for _ in range(N)]

    x, y = 0, 0
    idx = 0 # dx,dy돌릴 변수 : 우(y+1)->하(x+1)->좌(y-1)->상(x-1)

    dx = [0,1,0,-1] # 행이 x, 
    dy = [1,0,-1,0] # 열이 y

    for n in range(1, N*N+1):
        arr[x][y] = n
        x += dx[idx]
        y += dy[idx]
        
        # 부딪힌 경우(범위가 N or 0 or 이미 차있음) 방향 바꿔줘야 함
        # 아니지, 위에 실행한 것부터 다시 취소시켜야지 그 후에 방향 전환
        if x < 0 or x >= N or y < 0 or y >= N or arr[x][y] != 0:
            x -= dx[idx]
            y -= dy[idx]

            idx = (idx + 1) % 4 # N이 5 이상일 때부터 한 바퀴 이상 순환하니까..

            # for문 다음 거로 넘어가기 전에, 미리 여기서 추가시켜줘야 반복문 첫줄 제대로 실행 되겠지
            x += dx[idx]
            y += dy[idx]

    print(f'#{i}')
    for k in range(N):
        print(*arr[k])
