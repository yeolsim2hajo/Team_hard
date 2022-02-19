# split 사용해서, ''와 '1묶음'으로 나누기
# 가로찾기, 세로찾기 나눠서 각각 +
T = int(input())

for tc in range(1,T+1):
    N, K = map(int,input().split())

    arr = [input().replace(' ', '') for _ in range(N)]

    # 가로찾기
    cnt = 0
    for i in arr:
        for j in i.split('0'):
            if len(j) == K:
                cnt += 1

    # 세로찾기
    cnt_c = 0
    arr_c = [''.join(i) for i in list(zip(*arr))]
    for i in arr_c:
        for j in i.split('0'):
            if len(j) == K:
                cnt_c += 1

    print(f'#{tc}', cnt + cnt_c)
