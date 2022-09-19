# Contact
# for tc in range(1,11):
#     length, start = map(int,input().split())
#     data = list(map(int, input().split()))
#     link = [set() for _ in range(101)]
#     for i in range(0,length,2):
#         link[data[i]].add(data[i+1])
#     last = 0
#     def bfs():
#         global last
#         from collections import deque
#         q = deque()
#         q.append((start,0))
#         visited = [False] * 101
#         visited[start] = True
#         candidates = []
#         max_val = 0
#         while q:
#             number, time = q.popleft()
#             if time > max_val:
#                 max_val = time
#                 candidates = [number]
#             elif time == max_val:
#                 candidates.append(number)
#             for i in link[number]:
#                 if visited[i] is False:
#                     visited[i] = True
#                     q.append((i,time+1))
#         last = max(candidates)
#
#     bfs()
#     print(f'#{tc} {last}')


#재미있는 오셀로 게임
# T = int(input())
# for tc in range(1,1+T):
#     N, M = map(int, input().split())
#     board = [[0] * (N+2) for _ in range(N+2)]
#     board[N//2][N//2] = board[N//2 + 1][N//2 + 1] = 2
#     board[N//2][N//2 + 1] = board[N//2 + 1][N//2] = 1
#     color_cnt = [0,2,2]
#     for _ in range(M):
#         y, x, color = map(int,input().split())
#         color_cnt[color] += 1
#         for dy,dx in (-1,0),(1,0),(0,-1),(0,1):
#             ny,nx = y+dy,x+dx
#             cnt = 0
#             while 1 <= ny <= N and 1 <= nx <= N:
#                 if board[ny][nx] == 2//color:
#                     cnt += 1
#                     ny += dy
#                     nx += dx
#                 else:
#                     color_cnt[color] += cnt
#                     color_cnt[2//color] -= cnt
#                     for _ in range(cnt):
#                         ny -= dy
#                         nx -= dx
#                         board[ny][nx] = color
#                     break
#     print(f'#{tc} {color_cnt[1]} {color_cnt[2]}')


# 정식이의 은행 업무
# T = int(input())
# def to_three(result):
#     global answer
#     new_three = ''
#     var = result
#     while var:
#         new_three = str(var % 3) + new_three
#         var //= 3
#     if len(new_three) != len(three):
#         return
#     cnt = 0
#     for j in range(len(three)):
#         if new_three[j] != three[j]:
#             cnt += 1
#         if cnt > 2:
#             return
#     if cnt == 1:
#         answer = result
#
# def to_decimal():
#     for i in range(length - 1, -1, -1):
#         new = two[:]
#         new[i] = '0' if two[i] == '1' else '1'
#         power = 2 ** (length - 1)
#         result = 0
#         for number in new:
#             if number == '1':
#                 result += power
#             power //= 2
#         to_three(result)
#         if answer:
#             return
#
# for tc in range(1,T+1):
#     answer = 0
#     two = list(map(str,input()))
#     length = len(two)
#     three = input()
#     to_decimal()
#     print(f'#{tc} {answer}')



