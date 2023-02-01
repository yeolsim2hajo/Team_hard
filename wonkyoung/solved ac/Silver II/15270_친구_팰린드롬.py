#230201
# from sys import stdin
# new_input = stdin.readline
# N, M = map(int, new_input().split())
# if M == 0:
#     print(1)
# elif N <= 3:
#     for _ in range(M):
#         new_input()
#     print(N)
# else:
#     cnt = 0
#     relation = [[] for _ in range(21)]
#     visited = [False] * (N+1)
#     for _ in range(M):
#         person1, person2 = map(int, new_input().split())
#         if person1 > person2:
#             person1, person2 = person2, person1
#         relation[person1].append(person2)
#     def dfs(level, start, max_cnt):
#         global cnt
#         if cnt == N:
#             return
#         if max_cnt > cnt:
#             cnt = max_cnt
#         for i in range(start, N+1):
#             if not visited[i]:
#                 visited[i] = True
#                 for j in relation[i]:
#                     if not visited[j]:
#                         visited[j] = True
#                         dfs(level+1, i+1, max_cnt+2)
#                         visited[j] = False
#                 visited[i] = False
#     dfs(0, 1, 0)
#     if cnt < N and cnt % 2 == 0:
#         cnt += 1
#     print(cnt)


# 함수형
# def return_cnt():
#     from sys import stdin
#     new_input = stdin.readline
#     N, M = map(int, new_input().split())
#     if M == 0:
#         return 1
#     if N <= 3:
#         for _ in range(M):
#             new_input()
#         return N
#
#     cnt = 0
#     relation = [[] for _ in range(21)]
#     visited = [False] * (N+1)
#     for _ in range(M):
#         person1, person2 = map(int, new_input().split())
#         if person1 > person2:
#             person1, person2 = person2, person1
#         relation[person1].append(person2)
#
#     def dfs(level, start, max_cnt):
#         nonlocal cnt
#         if cnt == N:
#             return
#         if max_cnt > cnt:
#             cnt = max_cnt
#         for i in range(start, N+1):
#             if not visited[i]:
#                 visited[i] = True
#                 for j in relation[i]:
#                     if not visited[j]:
#                         visited[j] = True
#                         dfs(level+1, i+1, max_cnt+2)
#                         visited[j] = False
#                 visited[i] = False
#
#     dfs(0, 1, 0)
#     if cnt < N and cnt % 2 == 0:
#         return cnt + 1
#     return cnt
# print(return_cnt())


# input
def return_cnt():
    N, M = map(int, input().split())
    if M == 0:
        return 1
    if N <= 3:
        for _ in range(M):
            input()
        return N

    cnt = 0
    relation = [[] for _ in range(21)]
    visited = [False] * (N+1)
    for _ in range(M):
        person1, person2 = map(int, input().split())
        if person1 > person2:
            person1, person2 = person2, person1
        relation[person1].append(person2)

    def dfs(level, start, max_cnt):
        nonlocal cnt
        if cnt == N:
            return
        if max_cnt > cnt:
            cnt = max_cnt
        for i in range(start, N+1):
            if not visited[i]:
                visited[i] = True
                for j in relation[i]:
                    if not visited[j]:
                        visited[j] = True
                        dfs(level+1, i+1, max_cnt+2)
                        visited[j] = False
                visited[i] = False

    dfs(0, 1, 0)
    if cnt < N and cnt % 2 == 0:
        return cnt + 1
    return cnt
print(return_cnt())