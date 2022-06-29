#16951 블록 놀이
# N, K = map(int, input().split())
# tower = list(map(int, input().split()))
# min_cnt = N
# for i in range(N):
#     new_tower = tower[:]
#     cnt = 0
#     for j in range(i,0,-1):
#         if new_tower[j] - new_tower[j-1] != K:
#             cnt += 1
#             new_tower[j-1] = new_tower[j] - K
#             if new_tower[j-1] <= 0:
#                 break
#     else:
#         for j in range(i+1,N):
#             if new_tower[j] - new_tower[j-1] != K:
#                 cnt += 1
#                 new_tower[j] = new_tower[j-1] + K
#         if min_cnt > cnt:
#             min_cnt = cnt
#         # if min_cnt == 0:
#         #     break
# print(min_cnt)


#2531 회전 초밥
# set 사용 - 시간 많이 걸림
# N, number, dish, free = map(int, input().split())
# chobap = [input() for _ in range(N)]
# max_cnt = 0
# for i in range(N):
#     if i < N - dish:
#         case = set(chobap[i:i+dish])
#     else:
#         case = set(chobap[i:]+chobap[:i+dish-N])
#     case.add(free)
#     max_cnt = max(max_cnt, len(case))
# print(max_cnt)



# DAT 시간 초과
# N, number, dish, free = map(int, input().split())
# chobap = [int(input()) for _ in range(N)]
# max_cnt = 1
# for i in range(N):
#     check = [0] * (number+1)
#     cnt = 0
#     for j in range(dish):
#         idx = chobap[(i+j) % N]
#         if check[idx] == 0:
#             check[idx] = 1
#             cnt += 1
#     if check[free] == 0:
#         cnt += 1
#     if cnt > max_cnt:
#         max_cnt = cnt
# print(max_cnt)


#sliding window 사용
# N, number, dish, free = map(int, input().split())
# chobap = [int(input()) for _ in range(N)]
# check = [0] * (number+1)
# check[free] = max_cnt = 1
# for i in range(dish):
#     idx = chobap[i]
#     if check[idx] == 0:
#         max_cnt += 1
#     check[idx] += 1
# cnt = max_cnt
# for i in range(1,N):
#     pre = chobap[i-1]
#     next = chobap[(i + dish - 1)%N]
#     if check[pre] == 1:
#         cnt -= 1
#     check[pre] -= 1
#     if check[next] == 0:
#         cnt += 1
#     check[next] += 1
#     if cnt > max_cnt:
#         max_cnt = cnt
# print(max_cnt)

#sliding window + deque 사용 - 그냥 set보다 많이 걸림
# from collections import deque
# N, number, dish, free = map(int, input().split())
# chobap = [input() for _ in range(N)]
# case = deque(chobap[:dish])
# check = set(case + deque([free]))
# max_cnt = len(check)
# for i in range(1,N):
#     case.popleft()
#     case.append(chobap[(i + dish - 1)%N])
#     check = set(case + deque([free]))
#     max_cnt = max(len(check), max_cnt)
# print(max_cnt)

#sliding window 사용 + sys.stdin.readline
# import sys
# N, number, dish, free = map(int, input().split())
# new_input = sys.stdin.readline
# chobap = [int(new_input()) for _ in range(N)]
# check = [0] * (number+1)
# check[free] = max_cnt = 1
# for i in range(dish):
#     idx = chobap[i]
#     if check[idx] == 0:
#         max_cnt += 1
#     check[idx] += 1
# cnt = max_cnt
# for i in range(1,N):
#     pre = chobap[i-1]
#     next = chobap[(i + dish - 1)%N]
#     if check[pre] == 1:
#         cnt -= 1
#     check[pre] -= 1
#     if check[next] == 0:
#         cnt += 1
#     check[next] += 1
#     if cnt > max_cnt:
#         max_cnt = cnt
# print(max_cnt)