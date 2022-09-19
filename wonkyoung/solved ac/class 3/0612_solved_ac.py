# 6064 카잉달력
# 단순 - 시간 초과
# import sys
# T = int(input())
# new_input = sys.stdin.readline
# for _ in range(T):
#     M, N, x, y = map(int, new_input().split())
#     answer = -1
#     if x <= M and y <= N:
#         nx = ny = 1
#         answer += 2
#         while True:
#             if nx == x and ny == y:
#                 break
#             if nx == M and ny == N:
#                 answer = -1
#                 break
#             answer += 1
#             nx = nx+1 if nx < M else 1
#             ny = ny+1 if ny < N else 1
#     print(answer)

# 나머지 이용 - 느림 (1%)
# import sys
# T = int(input())
# new_input = sys.stdin.readline
# for _ in range(T):
#     M, N, x, y = map(int, new_input().split())
#     if x == y:
#         answer = x
#     else:
#         max_mod = N
#         start = 3
#         if N%2 == M%2 == 0:
#             start = 4
#         for i in range(start,M+1,2):
#             if N%i == M%i == 0:
#                 max_mod = N//i
#
#         if x == M and y == N:
#             answer = N * max_mod
#         else:
#             mod_x = 0
#             while mod_x < max_mod:
#                 answer = M * mod_x + x
#                 conf = answer % N
#                 if y == N and conf == 0:
#                     break
#                 if y == answer % N:
#                     break
#                 mod_x += 1
#             else:
#                 answer = -1
#     print(answer)


# 7569 토마토
# from collections import deque
# M, N, H = map(int,input().split())
# mature = deque()
# immature = set()
# for i in range(H):
#     for j in range(N):
#         box = input().split()
#         for k in range(M):
#             if box[k] == '1':
#                 mature.append((i, j, k, 0))
#             elif box[k] == '0':
#                 immature.add((i, j, k))
# if immature:
#     while mature:
#         h, r, c, day = mature.popleft()
#         for dh, dr, dc in (-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1):
#             nh, nr, nc = h+dh, r+dr, c+dc
#             if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M:
#                 if (nh, nr, nc) in immature:
#                     mature.append((nh, nr, nc, day + 1))
#                     immature.remove((nh, nr, nc))
#     if immature:
#         day = -1
# else:
#     day = 0
# print(day)



#7576 토마토 - 맞았지만 오래걸림 - new_input 효과 크지 않음
# from collections import deque
# import sys
# M, N= map(int,input().split())
# day = 0
# mature = deque()
# immature = set()
# new_input = sys.stdin.readline
# for i in range(N):
#     box = new_input().split()
#     for j in range(M):
#         if box[j] == '1':
#             mature.append((i, j, 0))
#         elif box[j] == '0':
#             immature.add((i, j))
# if immature:
#     while mature:
#         r, c, day = mature.popleft()
#         for dr, dc in (-1,0), (1,0), (0,-1), (0,1):
#             nr, nc = r+dr, c+dc
#             if 0 <= nr < N and 0 <= nc < M:
#                 if (nr, nc) in immature:
#                     mature.append((nr, nc, day + 1))
#                     immature.remove((nr, nc))
#     if immature:
#         day = -1
# print(day)


#7662 이중 우선순위 큐
# import sys
# from collections import deque
# T = int(input())
# new_input = sys.stdin.readline
# q = deque()
# length = 0
# for _ in range(T):
#     k = int(new_input())
#     for _ in range(k):
#         calc = new_input().split()
#         if calc[0] == 'I':
#             calc[1] = int(calc[1])
#             if length:
#                 position = length
#                 for i in range(length-1,-1,-1):
#                     if q[i] > calc[1]:
#                         position -= 1
#                     else:
#                         break
#                 q.insert(position,calc[1])
#             else:
#                 q.append(calc[1])
#             length += 1
#         elif q and calc[1] == '1':
#             q.pop()
#             length -= 1
#         elif q and calc[1] == '-1':
#             q.popleft()
#             length -= 1
#     answer = [q[-1], q[0]] if q else ['EMPTY']
#     print(*answer)

