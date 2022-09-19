#74 최장 경로 찾기 - 다시
# def bfs(a,b):
#     q = [graph[a]]
#     check = [0]*8
#     check[a] = 1
#     while q:
#         now = q.pop(0)
#         length = len(now)
#         for i in range(length):
#             node = now[i]
#             if node == b:
#                 check = [0] * 8
#                 check[a] = 1
#             if check[i] == 0:
#                 check[i] = 1
#                 node
#
#
# graph = {1: [2,3,4],
#          2: [1,3,4,5,6],
#          3: [1,2,7],
#          4: [1,2,5,6],
#          5: [2,4,6,7],
#          6: [2,4,5,7],
#          7: [3,5,6]}
# max_path = 0
# start,end = map(int, input().split())
# bfs(start,end)


#75 이상한 369 - 다시
# number = input()
# if int(number) < 10:
#     print(int(number)//3)
# else:
#     for n in number:
#         if int(n)%3:


#76 안전한 땅
# def bfs(y,x):
#     global max_tnt
#     q = [(y,x)]
#     dy = [1,0]
#     dx = [0,1]
#     visited = [[0]*a for _ in range(a)]
#     cnt = 0
#     while q:
#         nowy,nowx = q.pop(0)
#         if nowy == y+b-1 and nowx == x+b-1 and max_tnt < cnt:
#             max_tnt = cnt
#         for i in range(2):
#             ny = nowy+dy[i]
#             nx = nowx+dx[i]
#             if y <= ny < y+b and x <= nx < x+b:
#                 if visited[ny][nx] == 0:
#                     visited[ny][nx] = 1
#                     q.append((ny,nx))
#                     if city[ny][nx]:
#                         cnt += 1
#
# T = int(input())
# a, b = map(int, input().split())
# city = [list(map(int, input().split())) for _ in range(a)]
# max_tnt = 0
# for i in range(a-b+1):
#     for j in range(a-b+1):
#         bfs(i,j)
# print(max_tnt)


#77 가장 긴 공통 부분 문자열 - 다시

#78 원형 테이블
# def bfs():
#     q = [K]
#     numbers = q[:]
#     while q:
#         eat = q.pop(0)
#         if eat+K <= N:
#             q.append(eat+K-1)
#             numbers.append(eat+K-1)
#     print(numbers)
#
# N, K = map(int, input().split())
# bfs()


