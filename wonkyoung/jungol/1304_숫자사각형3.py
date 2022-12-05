#221205
# *
# N = int(input())
# numbers = [[0] * N for _ in range(N)]
# for j in range(N):
#     for i in range(N):
#         numbers[i][j] = N*j + i + 1
#
# for i in range(N):
#     print(*numbers[i])


# %, //
# N = int(input())
# numbers = [[0] * N for _ in range(N)]
# for i in range(N**2):
#     numbers[i%N][i//N] = i+1
#
# for i in range(N):
#     print(*numbers[i])


# N = int(input())
# numbers = [[0] * N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         print(i + j*N + 1, end=' ')
#     print()