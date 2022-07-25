# 사탕게임
# N x N 크기에 사탕을 채워 놓음
# 사탕의 색은 모두 같지 않을 수도 있다.
# 사탕의 색이 다른 인접한 두 칸을 고른다.
# 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다
# 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분을 고른 다음 그 사탕을 먹는다~
# 사탕을 먹을 수 있는 최대 개수를 구해라..

# 2중 for문 탐색


# 행, 열 방향으로 먹을 수 있는 최대 사탕 갯수를 반환하는 함수
def maxCandy():
    global N, bomboni
    row_eat, col_eat, row_max, col_max = 1, 1, -232323123, -12313123123123
    # 행
    for i in range(N):
        for k in range(N-1):
            if bomboni[i][k] == bomboni[i][k+1]:
                row_eat += 1
            else:
                row_eat = 1
            row_max = max(row_max, row_eat)
        row_eat = 1
    #열
    for i in range(N):
        for k in range(N-1):
            if bomboni[k][i] == bomboni[k+1][i]:
                col_eat += 1
            else:
                col_eat = 1
            col_max = max(col_eat, col_max)
        col_eat = 1

    max_candy = max(col_max, row_max)
    return max_candy

# direction 사용 -> 인접한 색이 다른 사탕을 swap하기 위해서 사용
N = int(input())
bomboni = [list(input()) for _ in range(N)]
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상 하 좌 우 탐색

# 2중for문 탐색
maxEatCandy = -12313212313
for i in range(N):
    for k in range(N):
        for d in range(4):
            new_y = i + direction[d][0]
            new_x = k + direction[d][1]
            # 범위 check
            if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N : continue
            # 사탕 색이 다르면 swap
            if bomboni[i][k] != bomboni[new_y][new_x]:
                bomboni[i][k], bomboni[new_y][new_x] = bomboni[new_y][new_x], bomboni[i][k]
                maxEatCandy = max(maxEatCandy, maxCandy()) # swap 후 먹을 수 있는 사탕 수를 검사 -> 새로운 max값이 나오면 maxEatCandy에 재할당
                bomboni[new_y][new_x], bomboni[i][k] = bomboni[i][k], bomboni[new_y][new_x] # swap 한 것을 다시 돌리기
            
print(maxEatCandy)