#230115
# T = int(input())
# def find_cnt(n, m):
#     cnt = 0
#     for i in range(1, n-1):
#         square_i = i * i
#         for j in range(i+1, n):
#             square_j = j * j
#             remain = (square_i + square_j + m)%(i*j)
#             if remain == 0:
#                 cnt += 1
#     return cnt
# for _ in range(T):
#     n, m = map(int, input().split())
#     print(find_cnt(n, m))


# new_input
# import sys
#
# new_input = sys.stdin.readline
# T = int(new_input())
# def find_cnt(n, m):
#     cnt = 0
#     for i in range(1, n-1):
#         square_i = i * i
#         for j in range(i+1, n):
#             square_j = j * j
#             remain = (square_i + square_j + m)%(i*j)
#             if remain == 0:
#                 cnt += 1
#     return cnt
# for _ in range(T):
#     n, m = map(int, new_input().split())
#     print(find_cnt(n, m))

# + m
import sys
new_input = sys.stdin.readline
T = int(new_input())
def find_cnt(n, m):
    cnt = 0
    for i in range(1, n-1):
        square_i = i * i + m
        for j in range(i+1, n):
            square_j = j * j
            remain = (square_i + square_j)%(i*j)
            if remain == 0:
                cnt += 1
    return cnt
for _ in range(T):
    n, m = map(int, new_input().split())
    print(find_cnt(n, m))