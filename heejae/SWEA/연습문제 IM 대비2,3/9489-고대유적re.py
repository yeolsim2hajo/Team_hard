
T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    max = 0
    # 가로 검사:
    for i in range(N):
        stack = 0
        for j in range(M):
            if arr[i][j] == 1:
                stack += 1
                if max < stack:
                    max = stack
            if arr[i][j] == 0:
                stack = 0
    # 세로 검사
    for i in range(M):
        stack = 0
        for j in range(N):
            if arr[j][i] == 1:
                stack += 1
                if max < stack:
                    max = stack
            if arr[j][i] == 0:
                stack = 0

    print(f'#{tc}', max)