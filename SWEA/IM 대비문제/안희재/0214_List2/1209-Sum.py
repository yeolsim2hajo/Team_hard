for i in range(1,11):
    case = int(input())
    arr = []
    for j in range(100):
        row = list(map(int,input().split()))
        arr.append(row)

    # 1. 행의 합 및 최댓값
    row_max = 0
    for j in range(100):
        row_sum = 0 # 계속 초기화시켜야 하니까, 이건 안에 넣어야 하지
        for k in range(100):
            row_sum += arr[j][k]
        if row_max < row_sum:
            row_max = row_sum

    # 2. 열의 합 및 최댓값
    column_max = 0
    for j in range(100):
        column_sum = 0 # 계속 초기화시켜야 하니까, 이건 안에 넣어야 하지
        for k in range(100):
            column_sum += arr[k][j]
        if column_max < column_sum:
            column_max = column_sum

    # 3. 대각선의 합
    for j in range(100):
        diagnoal = 0
        diagnoal += arr[j][j]

    print(f'#{i} {max(row_max, column_max, diagnoal)}')