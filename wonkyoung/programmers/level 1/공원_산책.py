#230324
# def solution(park, routes):
#     H, W = len(park), len(park[0])
#     def find_start():
#         for i in range(H):
#             for j in range(W):
#                 if park[i][j] == 'S':
#                     return i, j
#     y, x = find_start()
#     def apply_new(route):
#         nonlocal y, x
#         op, n = route.split()
#         n = int(n)
#         if op in {'E', 'W'}:
#             if op == 'E':
#                 nx = n+x
#                 if nx < W and 'X' not in park[y][x:nx+1]:
#                     x = nx
#             else:
#                 nx = -n+x
#                 if nx >= 0 and 'X' not in park[y][nx:x+1]:
#                     x = nx
#
#         elif op == 'S':
#             ny = n + y
#             if ny < H:
#                 for i in range(y, ny+1):
#                     if park[i][x] == 'X':
#                         break
#                 else:
#                     y = ny
#         else:
#             ny = -n + y
#             if 0 <= ny:
#                 for i in range(ny, y + 1):
#                     if park[i][x] == 'X':
#                         break
#                 else:
#                     y = ny
#
#     for route in routes:
#         apply_new(route)
#
#     return [y, x]
'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.04ms, 10.3MB)
테스트 4 〉	통과 (0.10ms, 10.2MB)
테스트 5 〉	통과 (0.13ms, 10.4MB)
테스트 6 〉	통과 (0.16ms, 10.2MB)
테스트 7 〉	통과 (0.22ms, 10.4MB)
테스트 8 〉	통과 (0.20ms, 10.4MB)
테스트 9 〉	통과 (0.17ms, 10.5MB)
테스트 10 〉	통과 (0.19ms, 10.5MB)
테스트 11 〉	통과 (0.11ms, 10.3MB)
테스트 12 〉	통과 (0.29ms, 10.3MB)
테스트 13 〉	통과 (0.19ms, 10.4MB)
테스트 14 〉	통과 (0.22ms, 10.4MB)
테스트 15 〉	통과 (0.26ms, 10.2MB)
테스트 16 〉	통과 (0.05ms, 10.5MB)
테스트 17 〉	통과 (0.05ms, 10.4MB)
테스트 18 〉	통과 (0.04ms, 10.5MB)
테스트 19 〉	통과 (0.08ms, 10.3MB)
테스트 20 〉	통과 (0.05ms, 10.4MB)
'''

#
# def solution(park, routes):
#
#     def find_start():
#         for i in range(H):
#             for j in range(W):
#                 if park[i][j] == 'S':
#                     return i, j
#
#     def apply_new(route):
#         nonlocal y, x
#         op, n = route.split()
#         n = int(n)
#         if op == 'E':
#             nx = n+x
#             if nx < W and 'X' not in park[y][x:nx+1]:
#                 x = nx
#         elif op == 'W':
#             nx = -n+x
#             if nx >= 0 and 'X' not in park[y][nx:x+1]:
#                 x = nx
#         elif op == 'S':
#             ny = n + y
#             if ny < H:
#                 for i in range(y, ny+1):
#                     if park[i][x] == 'X':
#                         break
#                 else:
#                     y = ny
#         else:
#             ny = -n + y
#             if 0 <= ny:
#                 for i in range(ny, y + 1):
#                     if park[i][x] == 'X':
#                         break
#                 else:
#                     y = ny
#     H, W = len(park), len(park[0])
#     y, x = find_start()
#     for route in routes:
#         apply_new(route)
#
#     return [y, x]
'''
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (0.08ms, 10.3MB)
테스트 5 〉	통과 (0.08ms, 10.4MB)
테스트 6 〉	통과 (0.32ms, 10.3MB)
테스트 7 〉	통과 (0.13ms, 10.4MB)
테스트 8 〉	통과 (0.11ms, 10.5MB)
테스트 9 〉	통과 (0.17ms, 10.3MB)
테스트 10 〉	통과 (0.10ms, 10.6MB)
테스트 11 〉	통과 (0.11ms, 10.6MB)
테스트 12 〉	통과 (0.16ms, 10.5MB)
테스트 13 〉	통과 (0.20ms, 10.5MB)
테스트 14 〉	통과 (0.11ms, 10.5MB)
테스트 15 〉	통과 (0.15ms, 10.3MB)
테스트 16 〉	통과 (0.04ms, 10.4MB)
테스트 17 〉	통과 (0.05ms, 10.5MB)
테스트 18 〉	통과 (0.04ms, 10.4MB)
테스트 19 〉	통과 (0.05ms, 10.3MB)
테스트 20 〉	통과 (0.07ms, 10.4MB)
'''

#
def solution(park, routes):
    def find_start():
        for i in range(H):
            for j in range(W):
                if park[i][j] == 'S':
                    return i, j

    def apply_new(route):
        nonlocal y, x
        op, n = route.split()
        n = int(n)
        dy, dx = direct[op]
        ny, nx = y+dy*n, x+dx*n
        if not (0 <= ny < H and 0 <= nx < W):
            return
        min_y, max_y = sorted((y, ny))
        min_x, max_x = sorted((x, nx))

        for i in range(min_y, max_y+1):
            for j in range(min_x, max_x+1):
                if park[i][j] == 'X':
                    return
        x, y = nx, ny

    H, W = len(park), len(park[0])
    y, x = find_start()
    direct = {'E': (0, 1), 'W': (0, -1), 'N': (-1, 0), 'S': (1, 0)}
    for route in routes:
        apply_new(route)

    return [y, x]
'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.5MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.4MB)
테스트 4 〉	통과 (0.09ms, 10.6MB)
테스트 5 〉	통과 (0.12ms, 10.4MB)
테스트 6 〉	통과 (0.24ms, 10.4MB)
테스트 7 〉	통과 (0.22ms, 10.4MB)
테스트 8 〉	통과 (0.18ms, 10.4MB)
테스트 9 〉	통과 (0.23ms, 10.5MB)
테스트 10 〉	통과 (0.16ms, 10.4MB)
테스트 11 〉	통과 (0.17ms, 10.4MB)
테스트 12 〉	통과 (0.23ms, 10.4MB)
테스트 13 〉	통과 (0.25ms, 10.3MB)
테스트 14 〉	통과 (0.16ms, 10.4MB)
테스트 15 〉	통과 (0.20ms, 10.5MB)
테스트 16 〉	통과 (0.08ms, 10.4MB)
테스트 17 〉	통과 (0.16ms, 10.4MB)
테스트 18 〉	통과 (0.05ms, 10.6MB)
테스트 19 〉	통과 (0.17ms, 10.5MB)
테스트 20 〉	통과 (0.07ms, 10.4MB)
'''