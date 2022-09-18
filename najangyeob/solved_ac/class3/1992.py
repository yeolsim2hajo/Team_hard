# BOJ 1992 - 쿼드 트리 - 분할 정복
import sys
input = sys.stdin.readline


def decompose(n, y, x):
    # print(n, y, x)
    if n == 1: # n이 1이면 더 나눠지지 않기 때문에 print
        print(image[y][x], end="")
        return

    flag = True
    for i in range(y, y+n):
        if not flag:
            break
        for j in range(x, x+n):
            if image[i][j] != image[y][x]:
                flag = False
                break

    if flag:
        print(image[y][x], end="")
    else:
        decreased_n = n//2

        print("(", end="")
        # 다른 숫자가 하나라도 있으면 4등분
        decompose(decreased_n, y, x)
        decompose(decreased_n, y, x+decreased_n)
        decompose(decreased_n, y+decreased_n, x)
        decompose(decreased_n, y+decreased_n, x+decreased_n)
        print(")", end="")


N = int(input())
image = [list(input().strip()) for _ in range(N)]
decompose(N, 0, 0)

# 분할 정복
# 0과 1로 이루어진 2차원 배열이 주어지고, 이 배열을 압축해서 표현
# 배열 전체가 0이면 0, 1이면 1
# 만약에 하나의 숫자로 표현하지 못하면 4등분
# 4등분 할때 '('를 추가한다
# 4등분 한 다음에 왼쪽 위부터 시계방향으로 조각난 배열이 1혹은 0으로만 이루어져 있는지 확인
# 순회가 끝나면 ')' 추가

