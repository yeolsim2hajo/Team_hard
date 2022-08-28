#1890 점프
# 메모리 초과
# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# def bfs():
#     from collections import deque
#     q = deque()
#     q.append((0,0))
#     cnt = 0
#     while q:
#         y, x = q.popleft()
#         number = board[y][x]
#         if y == x == N-1:
#             cnt += 1
#         elif number:
#             if y+number < N:
#                 q.append((y+number, x))
#             if x+number < N:
#                 q.append((y, x+number))
#     print(cnt)
# bfs()


# 시간 초과
# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# cnt = 0
# def dfs(y,x,value):
#     global cnt
#     if y == x == N-1:
#         cnt += 1
#         return
#     elif value == 0:
#         return
#     ny, nx = y+value, x+value
#     if ny < N:
#         dfs(ny, x, board[ny][x])
#     if nx < N:
#         dfs(y, nx, board[y][nx])
#
# dfs(0, 0, board[0][0])
# print(cnt)


#9933 민균이의 비밀번호
# sys.stdin.readline - 시간 줄어듦
# def password():
#     import sys
#     new_input = sys.stdin.readline
#     N = int(new_input())
#     check = {}
#     for _ in range(N):
#         word = new_input().rstrip()
#         if check.get(word) or word == word[::-1]:
#             return word
#         check[word[::-1]] = True
# answer = password()
# length = len(answer)
# print(length, answer[length//2])


# 시간, 메모리 같음
# def password():
#     import sys
#     new_input = sys.stdin.readline
#     N = int(new_input())
#     check = {}
#     for _ in range(N):
#         word = new_input().rstrip()
#         flip = word[::-1]
#         if check.get(word) or word == flip:
#             return word
#         check[flip] = True
# answer = password()
# length = len(answer)
# print(length, answer[length//2])

# 시간 더 걸림 (flip 있으면 시간 더 걸림)
# def password():
#     import sys
#     new_input = sys.stdin.readline
#     N = int(new_input())
#     check = {}
#     for _ in range(N):
#         word = new_input().rstrip()
#         check[word[::-1]] = True
#         if check.get(word):
#             return word
# answer = password()
# length = len(answer)
# print(length, answer[length//2])


# set - 시간 덜 걸림
# def password():
#     import sys
#     new_input = sys.stdin.readline
#     N = int(new_input())
#     check = set()
#     for _ in range(N):
#         word = new_input().rstrip()
#         check.add(word[::-1])
#         if word in check:
#             return word
# answer = password()
# length = len(answer)
# print(length, answer[length//2])


# 왜 시간 더 걸릴까
# def password():
#     import sys
#     new_input = sys.stdin.readline
#     N = int(new_input())
#     check = set()
#     for _ in range(N):
#         word = new_input().rstrip()
#         flip = word[::-1]
#         if word in check or word == flip:
#             return word
#         check.add(flip)
# answer = password()
# length = len(answer)
# print(length, answer[length//2])