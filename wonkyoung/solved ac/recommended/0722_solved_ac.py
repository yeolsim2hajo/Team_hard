#14425 문자열 집합
# import sys
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# S = {new_input() for _ in range(N)}
# cnt = 0
# for _ in range(M):
#     if new_input() in S:
#         cnt += 1
# print(cnt)

# 약간 시간 줄어듦
# import sys
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# S = {new_input():True for _ in range(N)}
# cnt = 0
# for _ in range(M):
#     if S.get(new_input()):
#         cnt += 1
# print(cnt)

# 시간 더 걸림
# from collections import defaultdict
# import sys
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# S = defaultdict(bool)
# for _ in range(N):
#     S[new_input().rstrip()] = True
# cnt = 0
# for _ in range(M):
#     if S[new_input().rstrip()]:
#         cnt += 1
# print(cnt)


#rstrip
# import sys
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# S = {new_input().rstrip() for _ in range(N)}
# cnt = 0
# for _ in range(M):
#     if new_input().rstrip() in S:
#         cnt += 1
# print(cnt)


#1495 기타리스트

# 시간 초과
# N, S, M = map(int,input().split())
# volumes = list(map(int,input().split()))
# q = [(S,0)]
# max_volume = -1
# while q:
#     now, idx = q.pop(0)
#     if idx == N:
#         if 0 <= now <= M and max_volume < now:
#             max_volume = now
#         continue
#     if 0 <= now+volumes[idx] <= M:
#         q.append((now+volumes[idx], idx+1))
#     if 0 <= now-volumes[idx] <= M:
#         q.append((now-volumes[idx], idx+1))
# print(max_volume)

#deque - 메모리 초과
# from collections import deque
# N, S, M = map(int,input().split())
# volumes = list(map(int,input().split()))
# q = deque([(S,0)])
# max_volume = -1
# while q:
#     now, idx = q.popleft()
#     if idx == N:
#         if 0 <= now <= M and max_volume < now:
#             max_volume = now
#         continue
#     if 0 <= now+volumes[idx] <= M:
#         q.append((now+volumes[idx], idx+1))
#     if 0 <= now-volumes[idx] <= M:
#         q.append((now-volumes[idx], idx+1))
# print(max_volume)


# 메모리 초과 - set으로 하면 TypeError
# N, S, M = map(int,input().split())
# volumes = list(map(int,input().split()))
# pre = [S]
# now = []
# for volume in volumes:
#     for number in pre:
#         if 0 <= number + volume <= M:
#             now.append(number + volume)
#         if 0 <= number - volume <= M:
#             now.append(number - volume)
#     pre = now[:]
#     now.clear()
# if pre:
#     print(max(pre))
# else:
#     print(-1)


# N, S, M = map(int,input().split())
# volumes = list(map(int,input().split()))
# pre = set(S)
# now = set()
# for volume in volumes:
#     for number in pre:
#         if 0 <= number + volume <= M:
#             now.add(number + volume)
#         if 0 <= number - volume <= M:
#             now.add(number - volume)
#     pre = set(now)
#     now.clear()
# if pre:
#     print(max(pre))
# else:
#     print(-1)

#dfs - 시간 초과
# N, S, M = map(int,input().split())
# volumes = list(map(int,input().split()))
# max_volume = -1
# def dfs(arg=0, now=S):
#     global max_volume
#     if not (0 <= now <= M):
#         return
#     if arg == N:
#         if max_volume < now:
#             max_volume = now
#         return
#     dfs(arg+1, now+volumes[arg])
#     dfs(arg+1, now-volumes[arg])
# dfs()
# print(max_volume)