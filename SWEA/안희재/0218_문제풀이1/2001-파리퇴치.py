# 파리채 크기 설정하는 함수 만들기
    # 특정 위치 주면, 그걸 기준으로 M*M파리채 만들고, 다 더해주기까지.
    # 해보니까, 굳이 direct로 할 필요가 없네
# (굳이)모든 좌표 검사(한 곳에 파리 몰려있을 수도 있으니..)
T = int(input())

for tc in range(1,T+1):
    arr = []
    N, M = map(int,input().split())
    for i in range(N):
        line = list(map(int,input().split()))
        arr.append(line)

    # 파리채로 잡은 파리개수 카운트하는 함수
    def catchmind(x,y, width): # width는 M, (x,y)는 좌표 / x는 행, y는 열
        sum = 0
        for i in range(width):
            for j in range(width):
                if x+i < N and y+j < N:
                    sum += arr[x+i][y+j]
        return sum

    # 모든 좌표에서 파리채함수 돌리기
    max = 0
    for i in range(N):
        for j in range(N):
            if catchmind(i,j, M) > max:
                max = catchmind(i,j, M)

    print(f'#{tc}', max)
