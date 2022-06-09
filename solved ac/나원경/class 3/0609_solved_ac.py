#1780 종이의 개수
# N = int(input())
# papers = []
# same = True
# for _ in range(N):
#     papers.append(input().split())
#     if same:
#         for i in range(N-1):
#             if papers[-1][i] != papers[-1][i+1]:
#                 same = False
#                 break
# numbers = [0]*3
# if same:
#     numbers[['-1', '0', '1'].index(papers[0][0])] = 1
#
# else:
#     def confirm(y,x,limit):
#         for dy in range(y,y+limit):
#             for dx in range(x,x+limit-1):
#                 if papers[dy][dx] != papers[dy][dx+1]:
#                     return False
#         return True
#
#     while True:
#         n = N//3
#         for i in range(0,N,n):
#             for j in range(0,N,n):
#                 same = confirm(i,j,n)
#
# print(*numbers, sep='\n')


#1927 최소 힙
# import sys
# N = int(input())
# new_input = sys.stdin.readline
# min_heap = [0]
# length = 1
# def push_num():
#     global length
#     min_heap.append(number)
#     var = length
#     while var > 1:
#         top = var //2
#         if min_heap[var] >= min_heap[top]:
#             break
#         min_heap[var], min_heap[top] = min_heap[top], min_heap[var]
#         var = top
#     length += 1
#
# def pop_num():
#     global length
#     min_heap[1], min_heap[-1] = min_heap[-1], min_heap[1]
#     print(min_heap.pop())
#     length -= 1
#     idx = 1
#     while idx < length//2:
#         if idx*2+1 < length:
#             bottom = idx*2+1 if min_heap[idx*2] > min_heap[idx*2+1] else idx*2
#         else:
#             bottom = idx*2
#         if min_heap[bottom] >= min_heap[idx]:
#             break
#         min_heap[idx], min_heap[bottom] = min_heap[bottom], min_heap[idx]
#         idx = bottom
#
# for _ in range(N):
#     number = int(new_input())
#     if number:
#         push_num()
#     elif len(min_heap) == 1:
#         print(0)
#     else:
#         pop_num()

#1931 회의실 배정 - 정렬
# import sys
# N = int(input())
# new_input = sys.stdin.readline
# conference = []
# for _ in range(N):
#     conference.append(list(map(int, new_input().split())))
# conference.sort(key=lambda x: (x[1], x[0]))
# now = conference[0]
# cnt = 1
# for i in range(1, N):
#     if now[1] <= conference[i][0]:
#         cnt += 1
#         now = conference[i]
# print(cnt)


# 재귀 이용 - 시간 초과
# import sys
# N = int(input())
# new_input = sys.stdin.readline
# conference = []
# for _ in range(N):
#     conference.append(list(map(int, new_input().split())))
# max_cnt = 1
# def dfs(arg, exclude, cnt):
#     global max_cnt
#     if cnt > max_cnt:
#         max_cnt = cnt
#     for j in range(N):
#         if conference[j][0] >= arg[1] and exclude != j:
#             visited[j] = True
#             dfs(conference[j],j,cnt+1)
#             visited[j] = False
# for i in range(N):
#     visited = [False] * N
#     visited[i] = True
#     dfs(conference[i],i,1)
# print(max_cnt)


#1992 쿼드트리

#2178 미로 탐색 - bfs
# N, M = map(int,input().split())
# maze = [input() for _ in range(N)]
# def bfs():
#     q = [(0, 0, 1)]
#     visited = [[False] * M for _ in range(N)]
#     visited[0][0] = True
#     while q:
#         y, x, cnt = q.pop(0)
#         if y == N-1 and x == M-1:
#             return cnt
#         for dy,dx in (-1,0),(1,0),(0,1),(0,-1):
#             ny, nx = y+dy, x+dx
#             if 0 <= ny < N and 0 <= nx < M:
#                 if maze[ny][nx] == '1' and not visited[ny][nx]:
#                     visited[ny][nx] = True
#                     q.append((ny, nx, cnt+1))
#
# print(bfs())

