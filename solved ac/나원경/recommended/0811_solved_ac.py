#16507 어두운 건 무서워
# import sys
#
# new_input = sys.stdin.readline
# R, C, Q = map(int, new_input().split())
# picture = []
# for _ in range(R):
#     picture.append(list(map(int, new_input().split())))
#     for j in range(1,C):
#         picture[-1][j] += picture[-1][j-1]
# for _ in range(Q):
#     r1, c1, r2, c2 = map(int, new_input().split())
#     total = 0
#     if r1 == 1:
#         if c1 > 1:
#             for i in range(r2):
#                 total += picture[i][c2 - 1] - picture[i][0]
#         else:
#             for i in range(r2):
#                 total += picture[i][c2 - 1]
#     elif c1 > 1:
#         for i in range(r1-1, r2):
#             total += picture[i][c2-1] - picture[i][c1-2]
#     else:
#         for i in range(r1 - 1, r2):
#             total += picture[i][c2 - 1] - picture[i][c1 - 2]
#     print(total//((r2-r1+1)*(c2-c1+1)))

#알파벳 개수
S = input()
check = [0]*26
order = [chr(ord('a') + i) for i in range(26)]
for alp in S:
    check[order.index(alp)] += 1
print(*check)
