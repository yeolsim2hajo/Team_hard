# n X m 직사각형
# 각 칸에는 한 자리의 숫자가 적혀있다
# 직사각형의 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하라
# 이 때, 정사각형은 행 또는 열에 평행 해야 한다

# 모든 좌표를 확인

import sys


n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int ,sys.stdin.readline().strip())) for _ in range(n)]
answer = []

for i in range(n):
    for j in range(m):
        target = graph[i][j] # 현재 꼭짓점에 쓰여 있는 수
        # 반복문을 통해 j축에 target과 똑같은 수를 확인
        for k in range(j, m):
            # target과 똑같은 수가 있다면 정사각형 위치가 범위 내에 있고 똑같은 수가 있는지 확인
            if graph[i][k] == target and i + k - j < n and k < m:
                if graph[i + k - j][j] == target and graph[i + k - j][k] == target:

                    # 정사각형 위치에 모두 똑같은 수가 있다면 길이를 제곱
                    answer.append((k - j + 1) ** 2)

# 제일 큰 정사각형의 크기를 출력
print(max(answer))