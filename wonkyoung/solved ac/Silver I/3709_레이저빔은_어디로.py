#221225
# import sys
# new_input = sys.stdin.readline
# convert = [1, 2, 3, 0]
# dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
# T = int(new_input())
# for _ in range(T):
#     N, R = map(int, new_input().split())
#     mirrors = set(tuple(map(int, new_input().split())) for _ in range(R))
#     x, y = map(int, new_input().split())
#     out = {0, N + 1}
#     index = 0
#     if x == 0:
#         index = 1
#     elif y == N+1:
#         index = 2
#     elif x == N+1:
#         index = 3
#     x += dx[index]
#     y += dy[index]
#     initial_x, initial_y, initial_i = x, y, index
#     while x not in out and y not in out:
#         if (x, y) in mirrors:
#             index = convert[index]
#         x += dx[index]
#         y += dy[index]
#         if initial_x == x and initial_y == y and initial_i == index:
#             x = y = 0
#             break
#     print(x, y)


# 함수
import sys
new_input = sys.stdin.readline
convert = [1, 2, 3, 0]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
def raiser():
    N, R = map(int, new_input().split())
    mirrors = set(tuple(map(int, new_input().split())) for _ in range(R))
    x, y = map(int, new_input().split())
    out = {0, N + 1}
    index = 0
    if x == 0:
        index = 1
    elif y == N + 1:
        index = 2
    elif x == N + 1:
        index = 3
    x += dx[index]
    y += dy[index]
    initial_x, initial_y, initial_i = x, y, index
    while x not in out and y not in out:
        if (x, y) in mirrors:
            index = convert[index]
        x += dx[index]
        y += dy[index]
        if initial_x == x and initial_y == y and initial_i == index:
            return '0 0'
    return f'{x} {y}'

T = int(new_input())
for _ in range(T):
    print(raiser())

