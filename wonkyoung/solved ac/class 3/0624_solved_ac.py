#10026 적록색약
# N = int(input())
# picture = [input() for _ in range(N)]
# cnt = [0]*2
# visited = [[False] * N for _ in range(N)]
#
# def bfs(*args):
#     from collections import deque
#     q = deque()
#     q.append(*args)
#     def iterate(option=0):
#         while q:
#             y, x = q.popleft()
#             for dy,dx in (-1,0), (1,0), (0,-1), (0,1):
#                 ny, nx = y+dy, x+dx
#                 if 0 <= ny < N and 0 <= nx < N:
#                     if visited[ny][nx] is False:
#                         if picture[ny][nx] == color:
#                             visited[ny][nx] = True
#                             q.append((ny, nx))
#                         elif option and picture[ny][nx] != 'B':
#                             visited[ny][nx] = True
#                             q.append((ny, nx))
#     if color == 'B':
#         iterate()
#         cnt[0] += 1
#         cnt[1] += 1
#     else:
#         iterate(1)
#
#
#
#
# for i in range(N):
#     for j in range(N):
#         if visited[i][j] is False:
#             color = picture[i][j]
#             bfs(i,j)
#
# visited = [[False] * N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         if picture[i][j] != 'B' and visited[i][j] is False:
#             color = picture[i][j]
#             bfs(i,j)
# print(*cnt)



#11659 구간 합 구하기 4 - 시간 초과
# import sys
#
# N, M = map(int, input().split())
# numbers = [0] + list(map(int, input().split()))
# new_input = sys.stdin.readline
# container = {(1, N): sum(numbers)}
# for _ in range(M):
#     start, end = map(int, new_input().split())
#     if start == end:
#         answer = numbers[start]
#     else:
#         if not container.get((start, end)):
#             container[(start, end)] = sum(numbers[start:end+1])
#         answer = container[(start, end)]
#     print(answer)


#15624 피보나치 수 7
# N = int(input())
# if N < 2:
#     print(N)
# else:
#     fibo = [0, 1]
#     for _ in range(1,N):
#         fibo[0], fibo[1] = fibo[1], fibo[0] + fibo[1]
#     print(fibo[-1]%1000000007)


# 메모리 초과
# import sys
#
# new_input = sys.stdin.readline
# fibo = [0,1]
# length = 2
# while True:
#     N = int(new_input())
#     if N >= length:
#         for _ in range(length,N+1):
#             fibo.append(fibo[-1] + fibo[-2])
#             length += 1
#     print(fibo[N]%1000000007)


#14594 동방 프로젝트 (Small)
N = int(input())
M = int(input())
cnt = N
if N:
    walls = [False] * N
    for _ in range(M):
        left, right = map(int,input().split())
        walls[left:right] = [True] * (right - left)
    for i in range(1, N):
        if walls[i] is True : cnt -= 1
print(cnt)

