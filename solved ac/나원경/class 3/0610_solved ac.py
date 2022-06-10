#2579 계단 오르기
# 시간 초과
# import sys
# N = int(input())
# new_input = sys.stdin.readline
# points = [int(new_input()) for _ in range(N)]
# max_point = 0
# def dfs(arg=0, cnt=0, total=0):
#     global max_point
#     if cnt >= 3:
#         return
#     if arg > N:
#         return
#     if arg == N:
#         if max_point < total:
#             max_point = total
#         return
#     dfs(arg+1,cnt+1,total+points[arg])
#     if arg < N-1:
#         dfs(arg+2,1,total+points[arg+1])
# dfs()
# print(max_point)

# bfs - 시간 초과
# import sys
# N = int(input())
# new_input = sys.stdin.readline
# points = [int(new_input()) for _ in range(N)]
# max_point = 0
# def bfs():
#     global max_point
#     q = [(0,0,0)]
#     while q:
#         step, cnt, total = q.pop(0)
#         if cnt < 3:
#             if step == N:
#                 if max_point < total:
#                     max_point = total
#                 continue
#             elif step > N:
#                 continue
#             q.append((step+1,cnt+1,total+points[step]))
#             if step < N-1:
#                 q.append((step+2,1,total+points[step+1]))
# bfs()
# print(max_point)


# 뒤에서부터 접근 - 시간 초과
# import sys
# N = int(input())
# new_input = sys.stdin.readline
# points = [int(new_input()) for _ in range(N)]
# points = [0] + points
# max_point = 0
# def bfs():
#     global max_point
#     q = [(N,1,points[N])]
#     while q:
#         step, cnt, total = q.pop(0)
#         if step < 0: continue
#         elif step == 0:
#             if max_point < total:
#                 max_point = total
#             continue
#         if cnt < 3:
#             q.append((step-1,cnt+1,total+points[step-1]))
#             if step > 1:
#                 q.append((step-2,1,total+points[step-2]))
# bfs()
# print(sum(points))
# print(max_point)


# 실패....
# import sys
# N = int(input())
# new_input = sys.stdin.readline
# points = [int(new_input()) for _ in range(N)]
# points = points
# point = points[-1]
# step = N-1
# cnt = 1
# while step:
#     if cnt == 3:
#         cnt = 1
#         step -= 2
#     if step == 1:
#         point += points[step-1]
#         break
#     elif points[step-1] <= points[step-2]:
#         cnt = 1
#         step -= 2
#     else:
#         cnt += 1
#         step -= 1
#     point += points[step]
# print(point)


#2606 바이러스
# computer = int(input())
# data = int(input())
# link_computer = [set() for _ in range(computer+1)]
# for _ in range(data):
#     one, two = map(int, input().split())
#     link_computer[one].add(two)
#     link_computer[two].add(one)
# visited = [False] * (computer+1)
# box = set()
# box.update(link_computer[1])
# cnt = 0
# visited[1] = True
# while box:
#     now = box.pop()
#     if visited[now] is False:
#         visited[now] = True
#         cnt += 1
#         box.update(link_computer[now])
# print(cnt)


#2667 단지번호 붙이기
# N = int(input())
# town = [input() for _ in range(N)]
# visited = [[False] * N for _ in range(N)]
# cnt_list = []
# def bfs(*args):
#     q = [args]
#     cnt = 1
#     while q:
#         y, x = q.pop(0)
#         for dy,dx in (-1,0),(1,0),(0,-1),(0,1):
#             ny, nx = y+dy, x+dx
#             if 0 <= ny < N and 0 <= nx < N:
#                 if visited[ny][nx] is False and town[ny][nx] == '1':
#                     visited[ny][nx] = True
#                     q.append((ny,nx))
#                     cnt += 1
#     cnt_list.append(cnt)
#
# for i in range(N):
#     for j in range(N):
#         if visited[i][j] is False and town[i][j] == '1':
#             visited[i][j] = True
#             bfs(i,j)
# print(len(cnt_list), *sorted(cnt_list), sep='\n')