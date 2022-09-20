# 와 진짜;; dfs 갓갓갓 알고리즘
# 최소한의 교체회수로 목적지(끝 인덱스)까지 도착해야 함
# return은 목적지 도달하는 경우에만. level대신 cnt변수 사용
# 일단, 처음 시작점은 무조건 고정
# 2 3 1 1의 경우
    # 처음 2에서 시작하면, -> 3 or 1을 선택할 수 있는 것!
    # 그 다음에 3을 선택하면, 1,1을 모두 선택 가능함 / 아니면 골인도 가능

T = int(input())
for tc in range(1,T+1):
    N, *arr = map(int,input().split())

    Min = 2e18
    def dfs(idx,cnt): # idx는 버스장류장 번호 / cnt는 배터리 교체 횟수
        global Min
        if Min < cnt: # 더 들어갈 필요도 없이 컷
            return 

        if idx >= N-1:
            if Min > cnt:
                Min = cnt
            return

        for i in range(idx+1,idx+1+arr[idx]): # 다음 시작점은 idx+1 // 충전지가 최대한 갈 수 있는 거리=arr[idx]
            dfs(i,cnt+1)
        
    dfs(0,0)
    print(f'#{tc} {Min-1}') # 첫 배터리의 경우 cnt 안하기 때문에 최종 결과에서 -1