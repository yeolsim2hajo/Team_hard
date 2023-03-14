#230314
# N = int(input())
# heights = [list(map(int, input().split())) for _ in range(N)]
# max_cnt = max_height = 1
# min_height = 100
# for i in range(N):
#     max_height = max(max_height, *heights[i])
#     min_height = min(min_height, *heights[i])
#
# def bfs(limit):
#     from collections import deque
#     visited = [[False] * N for _ in range(N)]
#     cnt = 0
#     q = deque()
#     for i in range(N):
#         for j in range(N):
#             if not visited[i][j]:
#                 visited[i][j] = True
#                 if heights[i][j] > limit:
#                     q.append((i, j))
#                     cnt += 1
#                     while q:
#                         y, x = q.popleft()
#                         for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
#                             ny, nx = y+dy, x+dx
#                             if 0 <= ny < N and 0 <= nx < N:
#                                 if not visited[ny][nx] and heights[ny][nx] > limit:
#                                     visited[ny][nx] = True
#                                     q.append((ny, nx))
#     return cnt
#
# for i in range(min_height, max_height):
#     cnt = bfs(i)
#     if cnt > max_cnt:
#         max_cnt = cnt
# print(max_cnt)


#
#
# from sys import stdin
# new_input = stdin.readline
# N = int(new_input())
# heights = [list(map(int, new_input().split())) for _ in range(N)]
# max_cnt = max_height = 1
# min_height = 100
# for i in range(N):
#     max_height = max(max_height, *heights[i])
#     min_height = min(min_height, *heights[i])
#
# def bfs(limit):
#     from collections import deque
#     visited = [[False] * N for _ in range(N)]
#     cnt = 0
#     q = deque()
#     for i in range(N):
#         for j in range(N):
#             if not visited[i][j]:
#                 visited[i][j] = True
#                 if heights[i][j] > limit:
#                     q.append((i, j))
#                     cnt += 1
#                     while q:
#                         y, x = q.popleft()
#                         for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
#                             ny, nx = y+dy, x+dx
#                             if 0 <= ny < N and 0 <= nx < N:
#                                 if not visited[ny][nx] and heights[ny][nx] > limit:
#                                     visited[ny][nx] = True
#                                     q.append((ny, nx))
#     return cnt
#
# for i in range(min_height, max_height):
#     cnt = bfs(i)
#     if cnt > max_cnt:
#         max_cnt = cnt
# print(max_cnt)


#
def find_safe_area():
    from sys import stdin
    new_input = stdin.readline
    N = int(new_input())
    heights = [list(map(int, new_input().split())) for _ in range(N)]

    max_cnt = max_height = 1
    min_height = 100
    for i in range(N):
        max_height = max(max_height, *heights[i])
        min_height = min(min_height, *heights[i])

    def bfs(*initial):
        from collections import deque
        q = deque()
        q.append(initial)
        while q:
            y, x = q.popleft()
            for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
                ny, nx = y+dy, x+dx
                if 0 <= ny < N and 0 <= nx < N:
                    if not visited[ny][nx] and heights[ny][nx] > limit:
                        visited[ny][nx] = True
                        q.append((ny, nx))

    for limit in range(min_height, max_height):
        cnt = 0
        visited = [[False] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    visited[i][j] = True
                    if heights[i][j] > limit:
                        cnt += 1
                        bfs(i, j)
        if cnt > max_cnt:
            max_cnt = cnt
    return max_cnt

print(find_safe_area())