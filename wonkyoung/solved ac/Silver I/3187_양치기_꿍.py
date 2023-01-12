#221225
# import sys
# from collections import deque
# new_input = sys.stdin.readline
# R, C = map(int, new_input().split())
# sheep, wolves, area = [], [], []
# dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
# for i in range(R):
#     row = new_input().rstrip()
#     area.append(row)
#     for j in range(C):
#         if row[j] == 'v':
#             wolves.append((i, j))
#         elif row[j] == 'k':
#             sheep.append((i, j))
#
# visited = [[False] * C for _ in range(R)]
# total_wolf = total_sheep = 0
# for y, x in wolves:
#     wolf_cnt, sheep_cnt = 1, 0
#     q = deque()
#     for i in range(4):
#         ny, nx = y+dy[i], x+dx[i]
#         if not visited[ny][nx]:
#             q.append((ny, nx))
#             visited[ny][nx] = True
#     visited[y][x] = True
#     while q:
#         ny, nx = q.popleft()
#         value = area[ny][nx]
#         if value == '#':
#             continue
#         elif value == 'v':
#             wolf_cnt += 1
#             wolves.remove((ny, nx))
#         elif value == 'k':
#             sheep_cnt += 1
#             sheep.remove((ny, nx))
#         for i in range(4):
#             next_y, next_x = ny+dy[i], nx+dx[i]
#             if not visited[next_y][next_x]:
#                 q.append((next_y, next_x))
#                 visited[next_y][next_x] = True
#     if wolf_cnt >= sheep_cnt:
#         total_wolf += wolf_cnt
#     else:
#         total_sheep += sheep_cnt
#
# print(total_sheep, total_wolf)


# dfs
import sys
new_input = sys.stdin.readline
R, C = map(int, new_input().split())
area = [list(map(str, new_input())) for _ in range(R)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
visited = [[False] * C for _ in range(R)]
total_wolf = total_sheep = 0
def dfs(y, x):
    global wolf_cnt, sheep_cnt
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        value = area[ny][nx]
        if not visited[ny][nx] and value != '#':
            visited[ny][nx] = True
            dfs(ny, nx)
            if value == 'v':
                wolf_cnt += 1
                area[ny][nx] = '.'
            elif value == 'k':
                sheep_cnt += 1
for i in range(R):
    for j in range(C):
        if area[i][j] == 'v':
            area[i][j] = '.'
            wolf_cnt, sheep_cnt = 1, 0
            visited[i][j] = True
            dfs(i, j)
            if wolf_cnt >= sheep_cnt:
                total_wolf += wolf_cnt
            else:
                total_sheep += sheep_cnt

print(total_sheep, total_wolf)




