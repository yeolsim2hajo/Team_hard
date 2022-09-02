#1025 제곱수 찾기
# from math import isqrt
# N, M = map(int, input().split())
# table = input().split()
# answer = -1
# def dfs(limit, option, index, level=0, dif=0, number=''):
#     global answer
#     if level == limit:
#         number, reversed_num = int(number), int(number[::-1])
#         root, reversed_root = isqrt(number), isqrt(reversed_num)
#         if number == root**2:
#             answer = max(answer, number)
#         if reversed_num == reversed_root**2:
#             answer = max(answer, reversed_num)
#         return
#     if option == 0:
#         for k in range(index+1, N):
#             if level != 0:
#                 if dif == k-index:
#                     dfs(limit, option, level+1, k, dif)
#             else:
#                 dfs(limit, option, level+1, k, k-index, number+str(k))
#     else:
#         for k in range(M):
#             pass
#
# for i in range(N-1, 0, -1):
#     for number in range(N-i):
#         dfs(i, 0, number)
# for j in range(M-1, 0, -1):
#     for number in range(M - j):
#         dfs(j, 1, number)


#1100 하얀 칸
def calc():
    chess = [input() for _ in range(8)]
    cnt = 0
    plus = {'.' : 0, 'F' : 1}
    for i in range(8):
        for j in range(8):
            if (i+j)%2 == 0:
                cnt += plus[chess[i][j]]
    return cnt
print(calc())
