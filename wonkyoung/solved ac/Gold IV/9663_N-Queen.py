#230115
# 시간 초과
# N = int(input())
# if N == 1:
#     print(1)
# else:
#     cnt = 0
#     path = []
#     def dfs(level):
#         global cnt
#         if level == N:
#             cnt += 1
#             return
#         for j in range(N):
#             dif, total = level-j, level+j
#             for i in range(level):
#                 y = path[i]
#                 if j == y or i-y == dif or y+i == total:
#                     break
#             else:
#                 path.append(j)
#                 dfs(level+1)
#                 path.pop()
#     dfs(0)
#     print(cnt)


# visited
# N = int(input())
# cnt = 0
# path = []
# visited = [False] * N
# def dfs(level):
#     global cnt
#     if level == N:
#         cnt += 1
#         return
#     for j in range(N):
#         if not visited[j]:
#             dif, total = level-j, level+j
#             for k in range(level):
#                 y, new_dif, new_total = path[k]
#                 if new_dif == dif or new_total == total:
#                     break
#             else:
#                 visited[j] = True
#                 path.append((j, dif, total))
#                 dfs(level+1)
#                 path.pop()
#                 visited[j] = False
# for i in range(N):
#     path.append((i, -i, i))
#     visited[i] = True
#     dfs(1)
#     visited[i] = False
#     path.pop()
# print(cnt)



# 대칭 - 시간 초과
# N = int(input())
# cnt = 0
# path = []
# visited = [False] * N
# def dfs(level):
#     global cnt
#     if level == N:
#         cnt += 1
#         return
#     for j in range(N):
#         if not visited[j]:
#             dif, total = level-j, level+j
#             for k in range(level):
#                 y, new_dif, new_total = path[k]
#                 if new_dif == dif or new_total == total:
#                     break
#             else:
#                 visited[j] = True
#                 path.append((j, dif, total))
#                 dfs(level+1)
#                 path.pop()
#                 visited[j] = False
#
#
# quot, remain = divmod(N, 2)
# for i in range(quot):
#     path.append((i, -i, i))
#     visited[i] = True
#     dfs(1)
#     visited[i] = False
#     path.pop()
# half_cnt = cnt
#
# cnt = 0
# if remain:
#     path.append((quot, -quot, quot))
#     visited[quot] = True
#     dfs(1)
#     visited[quot] = False
#     path.pop()
# print(2*half_cnt+cnt)


# dfs 말고 - 다시시
N= int(input())
cnt = path_length = 0
path = []
visited = [False] * N
quot, remain = divmod(N, 2)
for i in range(quot):
    path.append((i, -i, i))
    visited[i] = True
    for level in range(1, N):
        dif = total = level
        for j in range(N):
            dif -= 1
            total += 1
            if not visited[j]:
                for k in range(level):
                    y, new_dif, new_total = path[k]
                    if new_dif == dif or new_total == total:
                        break
                else:
                    visited[j] = True
                    path.append((j, dif, total))
                    path_length += 1
        if path_length < level:
            break
    else:
        cnt += 1

    visited[i] = False
    path.pop()
half_cnt = cnt

cnt = 0
if remain:
    path.append((quot, -quot, quot))
    visited[quot] = True
    dfs(1)
    visited[quot] = False
    path.pop()
print(2*half_cnt+cnt)