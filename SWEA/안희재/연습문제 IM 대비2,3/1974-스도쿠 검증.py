# 범위 내 합이 45면 sudoku!
T = int(input())

for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    # 가로 체크
    result = 1
    for i in range(9):
        sum = 0
        for j in range(9):
            sum += arr[i][j]
        if sum != 45:
            result = 0
            break
    # 세로 체크
    for i in range(9):
        sum = 0
        for j in range(9):
            sum += arr[j][i]
        if sum != 45:
            result = 0
            break
    # 격자 체크(1)
    def rectangle(x,y):
        dx = [0,0,0,1,1,1,2,2,2]
        dy = [0,1,2,0,1,2,0,1,2]
        sum = 0
        for i in range(9):
            sum += arr[x+dx[i]][y+dy[i]]
        if sum != 45:
            return 0
        else:
            return 1
    # 격자 체크(2)
    for i in range(0,7,3):
        for j in range(0,7,3):
            if rectangle(i,j) == 0:
                result = 0
                break

    print(f'#{tc}', result)