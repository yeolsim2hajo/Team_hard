# -----1트 : 실패
# N은 행, M은 열
# 가로탐색 vs 세로탐색 길이 비교해서 max
# 한 줄 탐색하다가, 1발견하면 카운트시작 / 1끊길때까지
T = int(input())

for tc in range(1, T+1):
    arr = []
    N, M = map(int,input().split())
    for i in range(N):
        line = list(map(int,input().split()))
        arr.append(line)

    # 가로 탐색
    max_r = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
            if j+1 == M:
                break
            if arr[i][j+1] == 0:
                cnt = 0
        if max_r < cnt:
            max_r = cnt

    # 세로 탐색
    max_c = 0
    for i in range(M):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            if j+1 == N:
                break
            if arr[j+1][i] == 0:
                cnt = 0
        if max_c < cnt:
            max_c = cnt

    print(f'#{tc}', max(max_r,max_c))

# 처음에 5/10만 성공 -> 아. 한 줄에 구조물이 2개이상 들어가있는 경우도 있잖아..
# 1 1 0 1 1 1
# 1 1 0 0 0 0
# 0 0 1 1 0 0
# 0 0 0 0 0 0
# 0 0 1 1 0 0
# -> 이 경우 3이 나와야 하는데, 2가 나옴
            # if j+1 == N or arr[j+1][i] == 0:
            #     break
            # 이게 아님
            # -----
            # if j+1 == N:
            #     break
            # if arr[j+1][i] == 0:
            #     cnt = 0
            # 근데 이것또한, 아님. 그 줄에서 앞쪽에 긴 구조물 있으면 어쩌려고?

# 이 논리가 아닌것 같음. 아무리 생각해도, 고려해야할 요소가 너무 많다
# 다시.