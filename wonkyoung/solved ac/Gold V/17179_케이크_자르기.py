#221223
# def find_max_val(cnt):
#     min_length = L // (cnt + 1)
#     between = [border[0]] * (M+1)
#     for i in range(1, M):
#         between[i] = border[i] - border[i-1]
#     between[M] = L - border[M-1]
#     if N == M:
#         return min(between)
#
# import sys
# new_input = sys.stdin.readline
# N, M, L = map(int, new_input().split())
# border = [int(new_input()) for _ in range(M)]
# for _ in range(N):
#     cnt = int(new_input())
#     find_max_val(cnt)

#221224
# def find_max_val(cnt):
#     min_length = L // (cnt + 1)
#     between = [border[0]] * (M+1)
#     for i in range(1, M):
#         between[i] = border[i] - border[i-1]
#     between[M] = L - border[M-1]
#     if N == M:
#         return min(between)
#
#
# import sys
# new_input = sys.stdin.readline
# N, M, L = map(int, new_input().split())
# border = [int(new_input()) for _ in range(M)]
# for _ in range(N):
#     cnt = int(new_input())
#     find_max_val(cnt)


#221231
#dfs - 44%에서 시간초과
# def find_dif(a, b):
#     return path[b] - path[a]
#
# def dfs(level=0, start=0):
#     global min_length
#     if level == cnt:
#         min_dif = L - path[-1]
#         for j in range(cnt):
#             min_dif = min(find_dif(j, j+1), min_dif)
#         min_length = max(min_dif, min_length)
#         return
#     for i in range(start, M):
#         path.append(position[i])
#         dfs(level+1, i+1)
#         path.pop()
#
# import sys
# new_input = sys.stdin.readline
# N, M, L = map(int, new_input().split())
# position = [int(new_input()) for _ in range(M)]
# for _ in range(N):
#     cnt = int(new_input())
#     path, min_length = [0], 0
#     dfs()
#     print(min_length)



# 이분 탐색

import sys
new_input = sys.stdin.readline
N, M, L = map(int, new_input().split())
position = set(int(new_input()) for _ in range(M))
for _ in range(N):
    cnt = int(new_input())
    div, min_length = L / (cnt+1), 0
    limit = [int(div * i) for i in range(1, M)]
    for i in range(M-1):
        start, end = 0, L
        while start <= end:
            mid = (start + end) // 2
            if mid in position:
    print(min_length)
