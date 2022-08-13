#16507 어두운 건 무서워
# 실패
# import sys
# import pprint
#
# new_input = sys.stdin.readline
# R, C, Q = map(int, new_input().split())
# acc = [[0]*(C+1)] + [[0] for _ in range(R)]
# for i in range(1, R+1):
#     acc[i] += list(map(int, new_input().split()))
#     for j in range(1,C+1):
#         acc[i][j] += acc[i-1][j]
# pprint.pprint(acc)
# for _ in range(Q):
#     r1, c1, r2, c2 = map(int, new_input().split())
#     print(acc[r2][c2], acc[r1][c1-1])
#     total = acc[r2][c2] - acc[r1][c1-1]
#     print(total, (r2-r1+1)*(c2-c1+1))
#     print(total//((r2-r1+1)*(c2-c1+1)))


# -1 연산 (시간, 메모리 더 나옴)
# import sys
#
# new_input = sys.stdin.readline
# R, C, Q = map(int, new_input().split())
# acc = []
# for _ in range(R):
#     acc.append(list(map(int, new_input().split())))
#     for j in range(1,C):
#         acc[-1][j] += acc[-1][j-1]
#
# for _ in range(Q):
#     r1, c1, r2, c2 = map(int, new_input().split())
#     total = 0
#     if c1 > 1:
#         for i in range(r1, r2+1):
#             total += acc[i-1][c2-1] - acc[i-1][c1-2]
#     else:
#         for i in range(r1, r2+1):
#             total += acc[i-1][c2-1]
#     print(total//((r2-r1+1)*(c2-c1+1)))


# 최적화
# import sys
# new_input = sys.stdin.readline
# R, C, Q = map(int, new_input().split())
# acc = [[0]*(C+1)] + [[0] for _ in range(R)]
# for i in range(1, R+1):
#     acc[i] += list(map(int, new_input().split()))
#     for j in range(1,C+1):
#         acc[i][j] += acc[i][j-1]
#     for j in range(1,C+1):
#         acc[i][j] += acc[i-1][j]
# for _ in range(Q):
#     r1, c1, r2, c2 = map(int, new_input().split())
#     total = acc[r2][c2] - acc[r1-1][c2] - acc[r2][c1-1] + acc[r1-1][c1-1]
#     print(total//((r2-r1+1)*(c2-c1+1)))

# 입력값을 picture에 넣기
import sys
new_input = sys.stdin.readline
R, C, Q = map(int, new_input().split())
acc = [[0]*(C+1)] + [[0] for _ in range(R)]
for i in range(1, R+1):
    picture = list(map(int, new_input().split()))
    acc[i] += picture
    for j in range(1,C+1):
        acc[i][j] += acc[i][j-1]
    for j in range(1,C+1):
        acc[i][j] += acc[i-1][j]
for _ in range(Q):
    r1, c1, r2, c2 = map(int, new_input().split())
    total = acc[r2][c2] - acc[r1-1][c2] - acc[r2][c1-1] + acc[r1-1][c1-1]
    print(total//((r2-r1+1)*(c2-c1+1)))

# [0] 나중에 더해주기
import sys
new_input = sys.stdin.readline
R, C, Q = map(int, new_input().split())
acc = [[0]*(C+1)]
for i in range(1, R+1):
    picture = [0] + list(map(int, new_input().split()))
    acc.append(picture)
    for j in range(1,C+1):
        acc[i][j] += acc[i][j-1]
    for j in range(1,C+1):
        acc[i][j] += acc[i-1][j]
for _ in range(Q):
    r1, c1, r2, c2 = map(int, new_input().split())
    total = acc[r2][c2] - acc[r1-1][c2] - acc[r2][c1-1] + acc[r1-1][c1-1]
    print(total//((r2-r1+1)*(c2-c1+1)))