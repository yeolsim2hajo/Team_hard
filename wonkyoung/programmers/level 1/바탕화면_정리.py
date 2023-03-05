#230306
# def solution(wallpaper):
#     row, col = len(wallpaper), len(wallpaper[0])
#     min_x, min_y = row, col
#     max_x = max_y = 0
#     for i in range(row):
#         for j in range(col):
#             if wallpaper[i][j] == '#':
#                 if min_x > i:
#                     min_x = i
#                 if min_y > j:
#                     min_y = j
#                 if max_x < i + 1:
#                     max_x = i + 1
#                 if max_y < j + 1:
#                     max_y = j + 1
#     return [min_x, min_y, max_x, max_y]
'''
테스트 1 〉	통과 (0.01ms, 10.4MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.07ms, 10.3MB)
테스트 8 〉	통과 (0.09ms, 10.1MB)
테스트 9 〉	통과 (0.17ms, 10.3MB)
테스트 10 〉	통과 (0.06ms, 10.4MB)
테스트 11 〉	통과 (0.04ms, 10.2MB)
테스트 12 〉	통과 (0.04ms, 10.2MB)
테스트 13 〉	통과 (0.04ms, 10.2MB)
테스트 14 〉	통과 (0.05ms, 10.3MB)
테스트 15 〉	통과 (0.08ms, 10.1MB)
테스트 16 〉	통과 (0.10ms, 10MB)
테스트 17 〉	통과 (0.03ms, 10.2MB)
테스트 18 〉	통과 (0.14ms, 10.3MB)
테스트 19 〉	통과 (0.09ms, 10.2MB)
테스트 20 〉	통과 (0.12ms, 10.2MB)
테스트 21 〉	통과 (0.01ms, 10.4MB)
테스트 22 〉	통과 (0.01ms, 10.3MB)
테스트 23 〉	통과 (0.01ms, 10.1MB)
테스트 24 〉	통과 (0.02ms, 10.2MB)
테스트 25 〉	통과 (0.21ms, 10.3MB)
테스트 26 〉	통과 (0.10ms, 10.2MB)
테스트 27 〉	통과 (0.06ms, 10.4MB)
테스트 28 〉	통과 (0.04ms, 10.4MB)
테스트 29 〉	통과 (0.06ms, 10.4MB)
테스트 30 〉	통과 (0.23ms, 10.2MB)
테스트 31 〉	통과 (0.14ms, 10.2MB)
'''

#
# def solution(wallpaper):
#     row, col = len(wallpaper), len(wallpaper[0])
#     min_x, min_y = row, col
#     max_x = max_y = 0
#     for i in range(row):
#         for j in range(col):
#             if wallpaper[i][j] == '#':
#                 if min_x == row:
#                     min_x = i
#                 if min_y > j:
#                     min_y = j
#                 if max_x < i + 1:
#                     max_x = i + 1
#                 if max_y < j + 1:
#                     max_y = j + 1
#     return [min_x, min_y, max_x, max_y]
'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.13ms, 10.4MB)
테스트 8 〉	통과 (0.09ms, 10.2MB)
테스트 9 〉	통과 (0.19ms, 10.3MB)
테스트 10 〉	통과 (0.11ms, 10.4MB)
테스트 11 〉	통과 (0.04ms, 10.3MB)
테스트 12 〉	통과 (0.04ms, 10.2MB)
테스트 13 〉	통과 (0.04ms, 10.2MB)
테스트 14 〉	통과 (0.05ms, 10.3MB)
테스트 15 〉	통과 (0.08ms, 10.3MB)
테스트 16 〉	통과 (0.11ms, 10.2MB)
테스트 17 〉	통과 (0.03ms, 10.1MB)
테스트 18 〉	통과 (0.14ms, 10.4MB)
테스트 19 〉	통과 (0.17ms, 10.3MB)
테스트 20 〉	통과 (0.13ms, 10.3MB)
테스트 21 〉	통과 (0.01ms, 10.2MB)
테스트 22 〉	통과 (0.01ms, 10.4MB)
테스트 23 〉	통과 (0.01ms, 10.2MB)
테스트 24 〉	통과 (0.02ms, 10.3MB)
테스트 25 〉	통과 (0.11ms, 10.2MB)
테스트 26 〉	통과 (0.10ms, 10.1MB)
테스트 27 〉	통과 (0.06ms, 10.3MB)
테스트 28 〉	통과 (0.03ms, 10.3MB)
테스트 29 〉	통과 (0.07ms, 10.4MB)
테스트 30 〉	통과 (0.24ms, 10.2MB)
테스트 31 〉	통과 (0.28ms, 10.2MB)
'''

#
def solution(wallpaper):
    row, col = len(wallpaper), len(wallpaper[0])
    min_x, min_y = row, col
    max_x = max_y = 0
    for i in range(row):
        if '#' in wallpaper[i]:
            min_x = i
            break
    for i in range(row-1, min_x-1, -1):
        if '#' in wallpaper[i]:
            max_x = i + 1
            break
    for j in range(col):
        for i in range(min_x, max_x):
            if wallpaper[i][j] == '#':
                min_y = j
                break
        if min_y == j:
            break
    for j in range(col-1, min_y-1, -1):
        for i in range(min_x, max_x):
            if wallpaper[i][j] == '#':
                max_y = j + 1
                break
        if max_y == j + 1:
            break
    return [min_x, min_y, max_x, max_y]
'''

테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.4MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.4MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.02ms, 10.3MB)
테스트 17 〉	통과 (0.01ms, 10.4MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.3MB)
테스트 20 〉	통과 (0.01ms, 10.2MB)
테스트 21 〉	통과 (0.01ms, 10.3MB)
테스트 22 〉	통과 (0.02ms, 10.4MB)
테스트 23 〉	통과 (0.01ms, 10.3MB)
테스트 24 〉	통과 (0.01ms, 10.4MB)
테스트 25 〉	통과 (0.04ms, 10.4MB)
테스트 26 〉	통과 (0.05ms, 10.2MB)
테스트 27 〉	통과 (0.05ms, 10.3MB)
테스트 28 〉	통과 (0.01ms, 10.3MB)
테스트 29 〉	통과 (0.01ms, 10.2MB)
테스트 30 〉	통과 (0.01ms, 10.2MB)
테스트 31 〉	통과 (0.02ms, 10.2MB)
'''