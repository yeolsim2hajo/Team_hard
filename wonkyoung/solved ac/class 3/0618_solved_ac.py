# 11724 연결 요소의 개수
# N, M = map(int,input().split())
# arr = [0] * (N+1)
# def find_link(x):
#     if arr[x] == 0:
#         arr[x] = x
#         return x
#     if arr[x] == x:
#         return x
#     return find_link(arr[x])
# def link(a,b):
#     f_a, f_b = find_link(a), find_link(b)
#     if f_a == f_b:
#         return
#     arr[b] = arr[f_b] = f_a
#
# for _ in range(M):
#     u, v = map(int,input().split())
#     link(u,v)
# print(arr)
# top = set()
# for i in range(1,N+1):
#     find_link(arr[i])
#     top.add(arr[i])
# print(len(top))


#11726 2xn 타일링 - 시간 초과
# n = int(input())
# if n in {1,2}:
#     print(n)
# else:
#     def bfs():
#         cnt = 0
#         q = [0]
#         while q:
#             total = q.pop(0)
#             if total > n:
#                 continue
#             if total == n:
#                 cnt += 1
#                 continue
#             for i in range(1,3):
#                 q.append(total+i)
#         return cnt
#     print(bfs())



#14500 테트로미노
# N, M = map(int,input().split())
# numbers = []
# # position = []
# max_val = 0
# for _ in range(N):
#     numbers.append(list(map(int,input().split())))
#     row_max = max(numbers[-1])
#     max_val = row_max if row_max > max_val else max_val
# max_total = 0
# def bfs(y,x):
#     global max_total
#     visited = [[False] * M for _ in range(N)]
#     visited[y][x] = True
#     q = [(y,x,1,numbers[y][x])]
#     while q:
#         now_y, now_x, cnt, total = q.pop(0)
#         if cnt == 4:
#             if total > max_total:
#                 max_total = total
#             continue
#         elif cnt == 3 and (max_total - total) >= max_val:
#             continue
#         for dy,dx in (1,0),(-1,0),(0,1),(0,-1):
#             ny,nx = now_y+dy, now_x+dx
#             if 0 <= ny < N and 0 <= nx < M:
#                 if visited[ny][nx] is False:
#                     visited[ny][nx] = True
#                     q.append((ny,nx,cnt+1,total+numbers[ny][nx]))
#
# # for i,j in position:
# for i in range(N):
#     for j in range(M):
#         bfs(i,j)
# print(max_total)


#16236 아기상어
# N = int(input())
# fish_position = []
# path = 0
# for i in range(N):
#     sea = list(map(int,input().split()))
#     for j in range(N):
#         if sea[j] == 9:
#             shark = (i,j)
#         elif sea[j] != 0:
#             fish_position.append((i,j, sea[j], 2))
# while fish_position:
#     y, x, fish, size = fish_position.pop(0)
#     for dy,dx in (-1,0), (1,0), (0,-1), (0,1):
#         ny, nx = y+dy, x+dx
#         if 0 <= ny < N and 0 <= nx < N:
#             if

# print(path)


#17219 비밀번호 찾기 - 변수에 넣든 안 넣든 메모리는 같음
# import sys
# N, M = map(int, input().split())
# new_input = sys.stdin.readline
# info = {}
# for _ in range(N):
#     key, value = new_input().split()
#     info[key] = value
# for _ in range(M):
#     # key = new_input().rstrip()
#     # print(info[key])
#
#     print(info[new_input().rstrip()])


#17626 Four Squares
# n = int(input())
# def find_number(target, end):
#     start = 1
#     while start <= end:
#         mid = (start + end) // 2
#         square = mid ** 2
#         if target == square:
#             return -2
#         elif target < square:
#             end = mid-1
#         else:
#             start = mid+1
#     return end
#
# limit = find_number(n,n)
# cnt = 4
# if limit != -2:
#     for i in range(limit, 0, -1):
#         target = n - (i**2)
#         if find_number(target, limit) == -2:
#             cnt = 2
#             break
#         elif cnt > 3:
#             for j in range(1,limit+1):
#                 new_target = target - (j**2)
#                 if new_target < 0:
#                     break
#                 if find_number(new_target, limit) == -2:
#                     cnt = 3
#                     break
# else:
#     cnt = 1
# print(cnt)
