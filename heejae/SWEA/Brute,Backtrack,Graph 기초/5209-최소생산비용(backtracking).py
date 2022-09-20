# dfs를 모르고 접근했다면, 각 공장별로 최소 비용인 것들 선택
    # 만약, 비용이 같은 것이 있다면 다음 제품으로 일단 pass,,,를 했을것 같다..
    # 코테갔을 때도, 어리버리 안하도록 dfs/bfs 등 여러 알고리즘 개념 착실히 손에 익혀두자
    # 또한, 백트랙킹은 코드의 실행시간을 줄일 수 있음! 중요중요!

# 핵심은, 각 공장당, 한 제품만 생산해야 한다는 것 -> used배열 사용
T = int(input())
for tc in range(1,T+1):
    N = int(input()) # N개의 제품과 공장들
    arr = [list(map(int,input().split())) for _ in range(N)]
    used = [0] * N # N개의 공장 사용여부

    Min = 2e18
    def dfs(level,Sum): # 레벨은 첫제품부터 ~ 끝제품까지
        global Min
        if Sum > Min: # 중간에 이미 최소비용 초과했으면 바로 컷
            return
        if level == N:
            if Min > Sum:
                Min = Sum
            return

        for i in range(N): # N개의 공장순회
            if used[i] == 0: # 재사용 방지
                used[i] = 1 # (i번째 공장 사용!)
                dfs(level+1,Sum+arr[level][i]) 
                used[i] = 0 # dfs빠져나올때는 다시 초기화

    dfs(0,0)
    print(f'#{tc} {Min}')
