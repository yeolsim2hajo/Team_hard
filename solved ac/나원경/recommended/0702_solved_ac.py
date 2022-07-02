#16960 스위치와 램프
# N, M = map(int, input().split())
# lamp = []
# for _ in range(N):
#     switch = list(map(int, input().split()))
#     lamp.append(switch[1:])
# all_lamp = set(range(1,M+1))
# for i in range(N):
#     except_one = set()
#     for j in range(N):
#         if i != j:
#             except_one.update(lamp[j])
#     if except_one == all_lamp:
#         print(1)
#         break
# else:
#     print(0)


# list comprehension
# N, M = map(int, input().split())
# lamp = [list(map(int, input().split()))[1:] for _ in range(N)]
# all_lamp = set(range(1,M+1))
# for i in range(N):
#     except_one = set()
#     for j in range(N):
#         if i != j:
#             except_one.update(lamp[j])
#     if except_one == all_lamp:
#         print(1)
#         break
# else:
#     print(0)


# sys.stdin.readline
# import sys
# N, M = map(int, input().split())
# new_input = sys.stdin.readline
# lamp = [list(map(int, new_input().split()))[1:] for _ in range(N)]
# all_lamp = set(range(1,M+1))
# for i in range(N):
#     except_one = set()
#     for j in range(N):
#         if i != j:
#             except_one.update(lamp[j])
#     if except_one == all_lamp:
#         print(1)
#         break
# else:
#     print(0)

# 리스트에 다 넣기
# import sys
# N, M = map(int, input().split())
# new_input = sys.stdin.readline
# lamp = []
# cnt = []
# for _ in range(N):
#     switch = list(map(int, new_input().split()))
#     lamp += switch[1:]
#     cnt.append(switch[0])
# all_lamp = set(range(1,M+1))
# for i in range(N):
#     start = sum(cnt[:i]) if i else 0
#     except_one = lamp[:]
#     for _ in range(cnt[i]):
#         except_one.pop(start)
#     if set(except_one) == all_lamp:
#         print(1)
#         break
# else:
#     print(0)


# 문자형으로 - 더 걸림
# import sys
# N, M = map(int, input().split())
# new_input = sys.stdin.readline
# lamp = []
# cnt = []
# for _ in range(N):
#     switch = new_input().split()
#     lamp += switch[1:]
#     cnt.append(int(switch[0]))
# all_lamp = set(map(str,range(1,M+1)))
# for i in range(N):
#     start = sum(cnt[:i]) if i else 0
#     except_one = lamp[:]
#     for _ in range(cnt[i]):
#         except_one.pop(start)
#     if set(except_one) == all_lamp:
#         print(1)
#         break
# else:
#     print(0)

# cnt가 누적합
# import sys
# N, M = map(int, input().split())
# new_input = sys.stdin.readline
# lamp = []
# cnt = []
# for _ in range(N):
#     switch = list(map(int, new_input().split()))
#     lamp += switch[1:]
#     if cnt:
#         cnt.append(switch[0] + cnt[-1])
#     else:
#         cnt.append(switch[0])
# all_lamp = set(range(1,M+1))
# for i in range(N):
#     start = cnt[i-1] if i else 0
#     except_one = lamp[:]
#     length = cnt[i] - cnt[i-1] if i else cnt[i]
#     for _ in range(length):
#         except_one.pop(start)
#     if set(except_one) == all_lamp:
#         print(1)
#         break
# else:
#     print(0)


# 뺐던 것 다시 넣기
# import sys
# N, M = map(int, input().split())
# new_input = sys.stdin.readline
# lamp = []
# cnt = []
# for _ in range(N):
#     switch = list(map(int, new_input().split()))
#     lamp += switch[1:]
#     if cnt:
#         cnt.append(switch[0] + cnt[-1])
#     else:
#         cnt.append(switch[0])
# all_lamp = set(range(1,M+1))
# for i in range(N):
#     start = cnt[i-1] if i else 0
#     except_one = []
#     length = cnt[i] - cnt[i-1] if i else cnt[i]
#     for _ in range(length):
#         except_one.append(lamp.pop(start))
#     if set(lamp) == all_lamp:
#         print(1)
#         break
#     for number in except_one:
#         lamp.insert(start, number)
# else:
#     print(0)


#20300 서강근육맨 - 시간 초과
# N = int(input())
# machine = list(map(int, input().split()))
# def bfs():
#     from collections import deque
#     q = deque()
#     for i in range(N):
#         number = machine[i]
#         q.append(({number}, i, number, number))
#     max_loss = [2e18] * N
#     while q:
#         path, idx, pre, total = q.popleft()
#         if total > max_loss[idx]:
#             continue
#         length = len(path)
#         for i in range(N):
#             now = machine[i]
#             if now not in path:
#                 if length%2:
#                     total = max(now+pre, total)
#                     if length == N-1:
#                         max_loss[idx] = min(max_loss[idx], total)
#                         continue
#                 elif length == N-1:
#                     total = max(now, total)
#                     max_loss[idx] = min(max_loss[idx], total)
#                     continue
#                 now_path = set(path)
#                 now_path.add(now)
#                 q.append((now_path, idx, now, total))
#     return min(max_loss)
#
# print(bfs())

# dfs - recursion error
# N = int(input())
# machine = list(map(int, input().split()))
# min_loss = 2e18
# visited = [False] * N
# def dfs(arg=0, total=0, pre=0):
#     global min_loss
#     if total > min_loss:
#         return
#     if arg == N:
#         if arg%2:
#             min_loss = min(min_loss, total, pre)
#         else:
#             min_loss = min(min_loss, total)
#         return
#     for i in range(N):
#         if visited[i] is False:
#             visited[i] = True
#             new_total = max(total, pre+machine[i]) if arg%2 else total
#             dfs(arg+1, new_total, machine[i])
#             visited[i] = False
# dfs()
# print(min_loss)


# sort
# N = int(input())
# machine = list(map(int, input().split()))
# machine.sort()
# min_loss = machine[-1]
# start = 0
# end = N-2 if N%2 else N-1
# while end >= start:
#     min_loss = max(machine[end] + machine[start], min_loss)
#     end -= 1
#     start += 1
# print(min_loss)


# 경우 나눔 - 시간 줄어들지 않음
# N = int(input())
# machine = list(map(int, input().split()))
# machine.sort()
# start = 1
# if N%2:
#     min_loss = max(machine[-1], machine[0] + machine[-2])
#     end = N-3
# else:
#     min_loss = machine[0] + machine[-1]
#     end = N-2
# while end >= start:
#     min_loss = max(machine[end] + machine[start], min_loss)
#     end -= 1
#     start += 1
# print(min_loss)