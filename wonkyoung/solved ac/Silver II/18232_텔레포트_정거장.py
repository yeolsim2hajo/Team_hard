#221218
# 시간 초과
# import sys
# from heapq import heappop, heappush
#
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# S, E = map(int, new_input().split())
# link = [set() for _ in range(N+1)]
# for _ in range(M):
#     start, end = map(int, new_input().split())
#     link[start].add(end)
#     link[end].add(start)
# heap = []
# heappush(heap, (0, S))
# while True:
#     cnt, now = heappop(heap)
#     if now == E:
#         break
#     next = set(link[now])
#     if now > 1:
#         next.add(now-1)
#     if now < N:
#         next.add(now+1)
#     for point in next:
#         heappush(heap, (cnt+1, point))
# print(cnt)



# visited 이용 + list
# import sys
# from heapq import heappop, heappush
#
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# S, E = map(int, new_input().split())
# link = [[] for _ in range(N+1)]
# visited = [False] * (N+1)
# for _ in range(M):
#     start, end = map(int, new_input().split())
#     link[start].append(end)
#     link[end].append(start)
# heap = []
# heappush(heap, (0, S))
# while True:
#     cnt, now = heappop(heap)
#     if now == E:
#         break
#     if not visited[now]:
#         visited[now] = True
#         if now > 1:
#             heappush(heap, (cnt+1, now-1))
#         if now < N:
#             heappush(heap, (cnt+1, now+1))
#         for point in link[now]:
#             heappush(heap, (cnt+1, point))
#
# print(cnt)


# 함수형
# def main():
#     import sys
#     from heapq import heappop, heappush
#
#     new_input = sys.stdin.readline
#     N, M = map(int, new_input().split())
#     S, E = map(int, new_input().split())
#     link = [[] for _ in range(N+1)]
#     visited = [False] * (N+1)
#     for _ in range(M):
#         start, end = map(int, new_input().split())
#         link[start].append(end)
#         link[end].append(start)
#
#     def find_min_cnt():
#         heap = []
#         heappush(heap, (0, S))
#         while True:
#             cnt, now = heappop(heap)
#             if now == E:
#                 return cnt
#             if not visited[now]:
#                 visited[now] = True
#                 if now > 1:
#                     heappush(heap, (cnt+1, now-1))
#                 if now < N:
#                     heappush(heap, (cnt+1, now+1))
#                 for point in link[now]:
#                     heappush(heap, (cnt+1, point))
#     return find_min_cnt()
# print(main())


# deque 사용 - 시간이 덜 걸림
# def main():
#     import sys
#     from collections import deque
#     new_input = sys.stdin.readline
#     N, M = map(int, new_input().split())
#     S, E = map(int, new_input().split())
#     link = [[] for _ in range(N+1)]
#     visited = [False] * (N+1)
#     for _ in range(M):
#         start, end = map(int, new_input().split())
#         link[start].append(end)
#         link[end].append(start)
#
#     def find_min_cnt():
#         q = deque([(0, S)])
#         while True:
#             cnt, now = q.popleft()
#             if now == E:
#                 return cnt
#             if not visited[now]:
#                 visited[now] = True
#                 if now > 1:
#                     q.append((cnt+1, now-1))
#                 if now < N:
#                     q.append((cnt+1, now+1))
#                 for point in link[now]:
#                     q.append((cnt+1, point))
#     return find_min_cnt()
# print(main())


# 함수 하나만 - 시간 더 걸림
# def find_min_cnt():
#     import sys
#     from collections import deque
#     new_input = sys.stdin.readline
#     N, M = map(int, new_input().split())
#     S, E = map(int, new_input().split())
#     link = [[] for _ in range(N+1)]
#     visited = [False] * (N+1)
#     for _ in range(M):
#         start, end = map(int, new_input().split())
#         link[start].append(end)
#         link[end].append(start)
#
#     q = deque([(0, S)])
#     while True:
#         cnt, now = q.popleft()
#         if now == E:
#             return cnt
#         if not visited[now]:
#             visited[now] = True
#             if now > 1:
#                 q.append((cnt+1, now-1))
#             if now < N:
#                 q.append((cnt+1, now+1))
#             for point in link[now]:
#                 q.append((cnt+1, point))
# print(find_min_cnt())


# 입력 받는 함수
# def main():
#     def fill_var():
#         import sys
#         new_input = sys.stdin.readline
#         N, M = map(int, new_input().split())
#         S, E = map(int, new_input().split())
#         link = [[] for _ in range(N+1)]
#         for _ in range(M):
#             start, end = map(int, new_input().split())
#             link[start].append(end)
#             link[end].append(start)
#         return (link, N, E, S)
#
#     link, N, E, S = fill_var()
#
#     def find_min_cnt():
#         from collections import deque
#         visited = [False] * (N + 1)
#         q = deque([(0, S)])
#         while True:
#             cnt, now = q.popleft()
#             if now == E:
#                 return cnt
#             if not visited[now]:
#                 visited[now] = True
#                 if now > 1:
#                     q.append((cnt+1, now-1))
#                 if now < N:
#                     q.append((cnt+1, now+1))
#                 for point in link[now]:
#                     q.append((cnt+1, point))
#     return find_min_cnt()
# print(main())


# list 대신 default dict
# def main():
#     import sys
#     new_input = sys.stdin.readline
#     N, M = map(int, new_input().split())
#     S, E = map(int, new_input().split())
#     link = {}
#     for _ in range(M):
#         start, end = map(int, new_input().split())
#         link.setdefault(start, [])
#         link.setdefault(end, [])
#         link[start].append(end)
#         link[end].append(start)
#
#     def find_min_cnt():
#         from collections import deque
#         visited = [False] * (N + 1)
#         q = deque([(0, S)])
#         while True:
#             cnt, now = q.popleft()
#             if now == E:
#                 return cnt
#             if not visited[now]:
#                 visited[now] = True
#                 if now > 1:
#                     q.append((cnt+1, now-1))
#                 if now < N:
#                     q.append((cnt+1, now+1))
#                 for point in link.get(now, []):
#                     q.append((cnt+1, point))
#     return find_min_cnt()
# print(main())


# 함수 X
# import sys
# new_input = sys.stdin.readline
# from collections import deque
# N, M = map(int, new_input().split())
# S, E = map(int, new_input().split())
# link = [[] for _ in range(N+1)]
# for _ in range(M):
#     start, end = map(int, new_input().split())
#     link[start].append(end)
#     link[end].append(start)
#
# visited = [False] * (N + 1)
# q = deque([(0, S)])
# while True:
#     cnt, now = q.popleft()
#     if now == E:
#         break
#     if not visited[now]:
#         visited[now] = True
#         if now > 1:
#             q.append((cnt+1, now-1))
#         if now < N:
#             q.append((cnt+1, now+1))
#         for point in link[now]:
#             q.append((cnt+1, point))
# print(cnt)


# deque X - 시간초과

# if문 변경
# def main():
#     import sys
#     new_input = sys.stdin.readline
#     N, M = map(int, new_input().split())
#     S, E = map(int, new_input().split())
#     link = [[] for _ in range(N+1)]
#     visited = [False] * (N+1)
#     for _ in range(M):
#         start, end = map(int, new_input().split())
#         link[start].append(end)
#         link[end].append(start)
#
#     def find_min_cnt():
#         from collections import deque
#         q = deque([(0, S)])
#         while True:
#             cnt, now = q.popleft()
#             if now == E:
#                 return cnt
#             if 1 <= now <= N and not visited[now]:
#                 visited[now] = True
#                 q.append((cnt+1, now-1))
#                 q.append((cnt+1, now+1))
#                 for point in link[now]:
#                     q.append((cnt+1, point))
#     return find_min_cnt()
# print(main())

# x-1, x+1 추가 - 메모리, 시간 증가
# def main():
#     import sys
#     new_input = sys.stdin.readline
#     N, M = map(int, new_input().split())
#     S, E = map(int, new_input().split())
#     link = [set() for _ in range(N+1)]
#     visited = [False] * (N+1)
#     for _ in range(M):
#         start, end = map(int, new_input().split())
#         link[start].add(end)
#         link[end].add(start)
#     for i in range(1, N):
#         link[i].add(i-1)
#         link[i].add(i+1)
#     link[0].add(1)
#     link[N].add(N-1)
#
#     def find_min_cnt():
#         from collections import deque
#         q = deque([(0, S)])
#         while True:
#             cnt, now = q.popleft()
#             if now == E:
#                 return cnt
#             if not visited[now]:
#                 visited[now] = True
#                 for point in link[now]:
#                     q.append((cnt+1, point))
#     return find_min_cnt()
# print(main())


# cnt += 1
# def main():
#     import sys
#     new_input = sys.stdin.readline
#     N, M = map(int, new_input().split())
#     S, E = map(int, new_input().split())
#     link = [[] for _ in range(N+1)]
#     visited = [False] * (N+1)
#     for _ in range(M):
#         start, end = map(int, new_input().split())
#         link[start].append(end)
#         link[end].append(start)
#
#     def find_min_cnt():
#         from collections import deque
#         q = deque([(0, S)])
#         while True:
#             cnt, now = q.popleft()
#             if now == E:
#                 return cnt
#             if 1 <= now <= N and not visited[now]:
#                 visited[now] = True
#                 new_cnt = cnt+1
#                 q.append((new_cnt, now-1))
#                 q.append((new_cnt, now+1))
#                 for point in link[now]:
#                     q.append((new_cnt, point))
#     return find_min_cnt()
# print(main())