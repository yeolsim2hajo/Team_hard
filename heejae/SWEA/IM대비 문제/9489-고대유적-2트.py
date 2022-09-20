# N은 행, M은 열
# 가로탐색 vs 세로탐색 길이 비교해서 max
# 한 줄 탐색하다가, 1발견하면 카운트시작 / 1끊길때까지
# 흠. 그냥 세로 정렬된 배열 또 하나 만들고, 그냥 함수 만들어서 돌려야겠다 
# 함수 변수에는 lst넣고 - tmp이용, "0 1 1 0 1 1 1 0 1 1 1 1" -> 4가 나오도록. ^오^ 성공
def longest(lst):
    cnt = 0
    tmp = 0
    for i in range(len(lst)):
        if lst[i] == 1:
            cnt += 1
        if i+1 == len(lst):
            return max(tmp,cnt)
        if lst[i+1] == 0:
            if tmp == 0: # tmp 아직 안 담겼다면?
                tmp = cnt # 임시로 담고, 초기화
                cnt = 0
            else: # tmp != 0 즉, 이전에 이미 담겼다면, tmp와 cnt 비교해서 갱신시키기
                if tmp < cnt:
                    tmp = cnt
                    cnt = 0

T = int(input())

for tc in range(1, T+1):
    arr = []
    N, M = map(int,input().split())
    for i in range(N):
        line = list(map(int,input().split()))
        arr.append(line)

    # 세로 정렬 리스트 만들기 - 가로줄 : M (원 배열은 가로줄 : N)
    arr_c = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            arr_c[i][j] = arr[j][i]

    max_r = 0
    for i in range(len(arr)):
        if longest(arr[i]) > max_r:
            max_r = longest(arr[i])
        
    max_c = 0
    for i in range(len(arr_c)):
        if longest(arr_c[i]) > max_c:
            max_c = longest(arr_c[i])
        
    print(f'#{tc}', max(max_r,max_c))

