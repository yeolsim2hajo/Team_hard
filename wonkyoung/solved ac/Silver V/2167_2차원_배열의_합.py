#230126
# import sys
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# arr = [[0] * (M+1)]
# for _ in range(N):
#     arr.append([0] + list(map(int, input().split())))
# acc = arr[:]
# for i in range(1, N+1):
#     for j in range(2, M+1):
#         acc[i][j] += acc[i][j-1]
# for j in range(1, M+1):
#     for i in range(2, N+1):
#         acc[i][j] += acc[i-1][j]
# K = int(new_input())
# for _ in range(K):
#     i, j, x, y = list(map(int, new_input().split()))
#     print(acc[x][y] - acc[x][j-1] - acc[i-1][y] + acc[i-1][j-1])

'''
3 3
1 2 4
8 16 32
9 1 2
4
1 1 2 3
1 2 1 2
1 3 3 3
2 2 3 3
'''


# 함수화
# def find_sum():
#     import sys
#     new_input = sys.stdin.readline
#     N, M = map(int, new_input().split())
#     arr = [[0] * (M+1)]
#     for _ in range(N):
#         arr.append([0] + list(map(int, input().split())))
#     acc = arr[:]
#     for i in range(1, N+1):
#         for j in range(2, M+1):
#             acc[i][j] += acc[i][j-1]
#     for j in range(1, M+1):
#         for i in range(2, N+1):
#             acc[i][j] += acc[i-1][j]
#     K = int(new_input())
#     for _ in range(K):
#         i, j, x, y = list(map(int, new_input().split()))
#         print(acc[x][y] - acc[x][j-1] - acc[i-1][y] + acc[i-1][j-1])
# find_sum()


#
def find_sum():
    def fill_arr():
        for _ in range(N):
            arr.append([0] + list(map(int, input().split())))
        for i in range(1, N+1):
            for j in range(2, M+1):
                arr[i][j] += arr[i][j-1]
        for j in range(1, M+1):
            for i in range(2, N+1):
                arr[i][j] += arr[i-1][j]
    import sys
    new_input = sys.stdin.readline
    N, M = map(int, new_input().split())
    arr = [[0] * (M+1)]
    fill_arr()
    K = int(new_input())
    for _ in range(K):
        i, j, x, y = list(map(int, new_input().split()))
        print(arr[x][y] - arr[x][j-1] - arr[i-1][y] + arr[i-1][j-1])
find_sum()
