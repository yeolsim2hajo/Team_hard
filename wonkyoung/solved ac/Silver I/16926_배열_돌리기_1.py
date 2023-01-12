#230111
# 입력 받기
import sys
new_input = sys.stdin.readline
N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 회전 한도 구하기
limit = N if N <= M else M
# R을 최소 회전 횟수로 바꿔주기
common_multiply = N*M
number = 1
for i in range(limit, 1, -1):
    if common_multiply%i == 0:
        common_multiply //= i
        number *= i
R %= number

