#16162 가희와 3단 고음
# N, A, D = map(int,input().split())
# scale = list(map(int,input().split()))
# now = A
# cnt = idx = 0
# while idx < N:
#     if now == scale[idx]:
#         now += D
#         cnt += 1
#     idx += 1
#
# print(cnt)


#17142 연구소3 -82까지 가고 틀림
# N, M = map(int, input().split())
# virus = []
# empty = set()
# for i in range(N):
#     state = input().split()
#     for j in range(N):
#         if state[j] == '2':
#             virus.append((i,j))
#         elif state[j] == '0':
#             empty.add((i,j))
# total_virus = len(virus)
# min_cnt = 1e8
# path = []
# def spread():
#     from collections import deque
#     q = deque(path)
#     space = {*empty}
#     while q:
#         y,x, time = q.popleft()
#         if time >= min_cnt:
#             return min_cnt
#         for dy, dx in (-1,0), (0,1), (1,0), (0,-1):
#             ny, nx = y+dy, x+dx
#             if (ny, nx) in space:
#                 space.remove((ny, nx))
#                 q.append((ny, nx, time+1))
#     if space:
#         return min_cnt
#     else:
#         return time
#
# def choose_virus(arg=0, start=0):
#     global min_cnt, path
#     if arg == M:
#         min_cnt = spread()
#         return
#     for i in range(start, total_virus):
#         path.append((*virus[i], 0))
#         choose_virus(arg+1, i+1)
#         path.pop()
#
# choose_virus()
# if min_cnt == 1e8:
#     min_cnt = -1
# print(min_cnt)