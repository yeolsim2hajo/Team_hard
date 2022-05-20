#11650 좌표 정렬하기
# 힙 정렬 구현
# N = int(input())
# points = [0]
# for i in range(1,N+1):
#     points.append(list(map(int,input().split())))
#     now = i
#     while now > 1:
#         parent = now//2
#         if points[now][0] > points[parent][0]:
#             break
#         elif points[now][0] == points[parent][0] and points[now][1] > points[parent][1]:
#             break
#         points[now], points[parent] = points[parent], points[now]
#         now = parent
# while len(points) > 1:
#     points[1], points[-1] = points[-1], points[1]
#     print(*points.pop())
#     now = 1
#     while True:
#         child = now*2
#         if child >= len(points):
#             break
#         elif child + 1 !=  len(points):
#             if points[child][0] > points[child+1][0]:
#                 child += 1
#             elif points[child][0] == points[child+1][0] and points[child][1] > points[child+1][1]:
#                 child += 1
#         if points[now][0] < points[child][0]:
#             break
#         elif points[now][0] == points[child][0] and points[now][1] < points[child][1]:
#             break
#         points[now], points[child] = points[child], points[now]
#         now = child
#
# N = int(input())
# positions = [list(map(int,input().split())) for _ in range(N)]
# positions.sort()
# for i in range(N):
#     print(*positions[i])