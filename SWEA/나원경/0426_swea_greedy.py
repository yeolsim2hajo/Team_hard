# 화물 도크
T = int(input())
for tc in range(1,1+T):
    N = int(input())
    reservation = [list(map(int, input().split())) for _ in range(N)]
    reservation.sort(key=lambda truck:truck[1])
    cnt = 1
    end = reservation[0][1]
    for i in range(1,N):
        if reservation[i][0] >= end:
            end = reservation[i][1]
            cnt += 1
    print(f'#{tc} {cnt}')