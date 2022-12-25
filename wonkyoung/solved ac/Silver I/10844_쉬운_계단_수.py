#221223
# dfs - 시간초과
# def find_step_number(N):
#     if N == 1:
#         return 9
#     next_num, length = [[] for _ in range(10)], [2] * 10
#     for i in range(10):
#         if 1 <= i < 9:
#             next_num[i].extend([i-1, i+1])
#         else:
#             next_num[i].append(i - 1 if i == 9 else i + 1)
#             length[i] = 1
#
#     cnt = 0
#     def dfs(level, now):
#         nonlocal cnt
#         if level == N-2:
#             cnt += length[now]
#             return
#         for j in next_num[now]:
#             dfs(level+1, j)
#
#     for i in range(1, 10):
#         dfs(0, i)
#     return int(cnt%1e9)
#
# N = int(input())
# print(find_step_number(N))


# dp
# def find_step_number(N):
#     if N == 1:
#         return 9
#     next_num, length = [[] for _ in range(10)], [2] * 10
#     for i in range(10):
#         if 1 <= i < 9:
#             next_num[i].extend([i-1, i+1])
#         else:
#             next_num[i].append(i - 1 if i == 9 else i + 1)
#             length[i] = 1
#
#     cnt = 0
#     def dfs(level, now):
#         nonlocal cnt
#         if level == N-2:
#             cnt += length[now]
#             return
#         for j in next_num[now]:
#             dfs(level+1, j)
#
#     for i in range(1, 10):
#         dfs(0, i)
#     return int(cnt%1e9)
#
# N = int(input())
# print(find_step_number(N))


# bfs - 메모리 초과
# def find_step_number(N):
#     if N == 1:
#         return 9
#     next_num, length = {str(i):[] for i in range(10)}, [2] * 10
#     for i in range(10):
#         key = str(i)
#         if 1 <= i < 9:
#             next_num[key].extend([str(i-1), str(i+1)])
#         else:
#             next_num[key].append('8' if i == 9 else '1')
#             length[i] = 1
#
#     cnt = 0
#     def bfs(first):
#         from collections import deque
#         cnt = 0
#         q = deque([(1, str(first))])
#         while q:
#             length, number = q.popleft()
#             if length == N:
#                 cnt += 1
#             elif length < N:
#                 length += 1
#                 last = number[-1]
#                 for j in next_num[last]:
#                     q.append((length, number+j))
#         return int(cnt%1e9)
#
#     for i in range(1, 10):
#         cnt += bfs(i)
#     return int(cnt%1e9)
#
# N = int(input())
# print(find_step_number(N))


# 221225
# def find_step_number(N):
#     if N == 1:
#         return 9
#     if N == 2:
#         return 17
#     next_num, length = [[] for _ in range(10)], [2] * 10
#     for i in range(10):
#         if 1 <= i < 9:
#             next_num[i].extend([i-1, i+1])
#         else:
#             next_num[i].append(i - 1 if i == 9 else i + 1)
#             length[i] = 1
#
#     def div(number):
#         return int(number%1e9)
#     # 자리 수
#     for _ in range(2, N):
#         temp = [0] * 10
#         # 첫 번째 숫자
#         for i in range(0, 10):
#             # 다음 숫자
#             for j in next_num[i]:
#                 temp[i] += length[j]
#         length = list(map(div, temp))
#         # print(_, length)
#     return int(sum(length[1:])%1e9)
#
# N = int(input())
# print(find_step_number(N))


# 짧게
def find_step_number(N):
    if N == 1:
        return 9
    next_num, length = [[i-1, i+1] if 1 <= i < 9 else [i - 1 if i == 9 else i + 1] for i in range(10)], [2] * 10
    length[0] = length[9] = 1

    def div(number):
        return int(number%1e9)
    for _ in range(2, N):
        temp = [0] * 10
        for i in range(0, 10):
            for j in next_num[i]:
                temp[i] += length[j]
        length = list(map(div, temp))
    return div(sum(length[1:]))

N = int(input())
print(find_step_number(N))