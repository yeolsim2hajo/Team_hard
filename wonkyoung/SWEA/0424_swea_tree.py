# Contact
# def contact():
#     from collections import deque
#     global last
#     q = deque()
#     q.append((start, 0))
#     max_cnt = 0
#     while q:
#         idx, cnt = q.popleft()
#         if max_cnt < cnt or (max_cnt == cnt and last < idx):
#             last = idx
#             max_cnt = cnt
#         if link.get(idx):
#             length = len(link[idx])
#             for _ in range(length):
#                 next = link[idx].pop()
#                 if visited[next] == False:
#                     visited[next] = True
#                     q.append((next, cnt+1))
#
# for tc in range(1,11):
#     length, start = map(int,input().split())
#     data = list(map(int,input().split()))
#     link = {}
#     for i in range(0,length,2):
#         idx = data[i]
#         if link.get(idx):
#             link[idx].add(data[i+1])
#         else:
#             link[idx] = {data[i+1]}
#     visited = [False]*101
#     visited[start] = True
#     last = start
#     contact()
#     print(f'#{tc} {last}')

