# 아 인접행렬 그래프..구나;; 무슨 문제인가 했네;;
# 경로는 항상 e[1][2]+e[2][3]+e[3][1]
    # 위처럼, x좌표 시작은 1, 끝의 y좌표는 1!
# 9 -> (14x) 27 -> 24(0은 x) -> 
# 자기자신, 그리고 전의 문으로 되돌아가지못함
# 마지막은 항상 1로 가야함
# 아, 각 구역은 한번씩만 방문해야함;; -> visit...
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    path = [0] * N
    visit = [0] * N
    visit[0] = 1

    Min = 2e18
    def dfs(level,next):
        global Min
        # if level == N: -> 이 문제는, 마지막 돌아갈 곳이 정해져있으므로, N이 아니라 N-1임
        #     if sum(path) < Min:
        #         Min = sum(path)
        #     return

        if level == N-1:
            path[level] = arr[next][0] # 마지막엔, 사무실(1)로 back
            if sum(path) < Min:
                Min = sum(path)
                return
        else:
            for i in range(N):
                if visit[i] == 0 and i != next and i != 0: # 마지막 전에는, 1번사무실로 돌아오면 안됨!(=0번인덱스 컷)
                    path[level] = arr[next][i]
                    visit[i] = 1 # 재방문 방지용
                    dfs(level+1,i) # door가 이전이 됨.
                    visit[i] = 0

    dfs(0,0)
    print(f'#{tc} {Min}')