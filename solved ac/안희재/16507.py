# 일일이 전부 더함 -> 시간초과
    # 구간합으로 해결 -> 계산작업의 간소화
    # 2차원 배열의 구간합 문제는 반복 연습 필요!

import sys

input = sys.stdin.readline
R, C, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
prefix_arr = [[0] * (C + 1) for _ in range(R + 1)] # 구간합 배열 -> (1,1)좌표는 실제 처음 지점(인덱스로 치면 0,0)이므로 R+1,C+1 칸을 만들어 줌

for i in range(1, R + 1):
    for j in range(1, C + 1):
        prefix_arr[i][j] = prefix_arr[i - 1][j] + prefix_arr[i][j - 1] + arr[i - 1][j - 1] - prefix_arr[i - 1][j - 1]
        # prefix_arr[i][j]는 (1,1)부터 (i,j)까지의 합 -> 1차원 배열 응용

for _ in range(Q): 
    r1, c1, r2, c2 = map(int, input().split())
    sum = prefix_arr[r2][c2] - prefix_arr[r1 - 1][c2] - prefix_arr[r2][c1 - 1] + prefix_arr[r1 - 1][c1 - 1]
    print(sum // ((r2 - r1 + 1) * (c2 - c1 + 1)))