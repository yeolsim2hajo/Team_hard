#230302
# def solution(N, road, K):
#     answer = 0
#     unlink = int(5e5) + 1
#     time_table = [[unlink] * (N+1) for _ in range(N+1)]
#     for i in range(1, N+1):
#         time_table[i][i] = 0
#
#     for a, b, c in road:
#         if time_table[a][b] > c:
#             time_table[a][b] = c
#             time_table[b][a] = c
#     for via in range(1, N+1):
#         for start in range(1, N+1):
#             for end in range(1, N+1):
#                 time_table[start][end] = min(time_table[start][end], time_table[start][via] + time_table[via][end])
#
#     for i in range(1, N+1):
#         if time_table[1][i] <= K:
#             answer += 1
#     return answer

# print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
# print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))
'''
테스트 1 〉	통과 (0.12ms, 10.3MB)
테스트 2 〉	통과 (0.06ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.30ms, 10.2MB)
테스트 6 〉	통과 (0.08ms, 10.2MB)
테스트 7 〉	통과 (0.08ms, 10.3MB)
테스트 8 〉	통과 (0.08ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.23ms, 10.2MB)
테스트 11 〉	통과 (0.31ms, 10.4MB)
테스트 12 〉	통과 (17.24ms, 10.3MB)
테스트 13 〉	통과 (9.78ms, 10.3MB)
테스트 14 〉	통과 (11.33ms, 10.3MB)
테스트 15 〉	통과 (15.23ms, 10.2MB)
테스트 16 〉	통과 (2.14ms, 10.3MB)
테스트 17 〉	통과 (12.08ms, 10.3MB)
테스트 18 〉	통과 (47.88ms, 10.3MB)
테스트 19 〉	통과 (29.24ms, 10.3MB)
테스트 20 〉	통과 (32.56ms, 10.3MB)
테스트 21 〉	통과 (39.95ms, 10.6MB)
테스트 22 〉	통과 (35.43ms, 10.1MB)
테스트 23 〉	통과 (35.77ms, 10.4MB)
테스트 24 〉	통과 (28.31ms, 10.4MB)
테스트 25 〉	통과 (60.46ms, 10.5MB)
테스트 26 〉	통과 (36.12ms, 10.4MB)
테스트 27 〉	통과 (50.71ms, 10.4MB)
테스트 28 〉	통과 (42.87ms, 10.6MB)
테스트 29 〉	통과 (39.05ms, 10.3MB)
테스트 30 〉	통과 (40.33ms, 10.4MB)
테스트 31 〉	통과 (35.84ms, 10.2MB)
테스트 32 〉	통과 (42.91ms, 10.3MB)
'''

#
# def solution(N, road, K):
#     answer = 0
#     unlink = int(5e5) + 1
#     time_table = [[unlink] * (N+1) for _ in range(N+1)]
#     for i in range(1, N+1):
#         time_table[i][i] = 0
#
#     for a, b, c in road:
#         if time_table[a][b] > c:
#             time_table[a][b] = c
#             time_table[b][a] = c
#     for via in range(1, N+1):
#         for start in range(1, N+1):
#             if via != start:
#                 for end in range(1, N+1):
#                     if via != end != start:
#                         time_table[start][end] = min(time_table[start][end], time_table[start][via] + time_table[via][end])
#
#     for i in range(1, N+1):
#         if time_table[1][i] <= K:
#             answer += 1
#     return answer
'''
테스트 1 〉	통과 (0.11ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.04ms, 10.4MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.26ms, 10.4MB)
테스트 6 〉	통과 (0.06ms, 10.3MB)
테스트 7 〉	통과 (0.06ms, 10.3MB)
테스트 8 〉	통과 (0.06ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.22ms, 10.3MB)
테스트 11 〉	통과 (0.27ms, 10.1MB)
테스트 12 〉	통과 (16.72ms, 10.4MB)
테스트 13 〉	통과 (17.86ms, 10.2MB)
테스트 14 〉	통과 (9.88ms, 10.4MB)
테스트 15 〉	통과 (16.63ms, 10.4MB)
테스트 16 〉	통과 (2.00ms, 10.3MB)
테스트 17 〉	통과 (7.38ms, 10.3MB)
테스트 18 〉	통과 (39.54ms, 10.1MB)
테스트 19 〉	통과 (34.04ms, 10.5MB)
테스트 20 〉	통과 (35.73ms, 10.3MB)
테스트 21 〉	통과 (29.53ms, 10.5MB)
테스트 22 〉	통과 (58.05ms, 10.4MB)
테스트 23 〉	통과 (38.35ms, 10.4MB)
테스트 24 〉	통과 (29.28ms, 10.3MB)
테스트 25 〉	통과 (49.63ms, 10.6MB)
테스트 26 〉	통과 (47.40ms, 10.7MB)
테스트 27 〉	통과 (48.39ms, 10.5MB)
테스트 28 〉	통과 (47.64ms, 10.6MB)
테스트 29 〉	통과 (63.43ms, 10.5MB)
테스트 30 〉	통과 (42.33ms, 10.3MB)
테스트 31 〉	통과 (39.65ms, 10.4MB)
테스트 32 〉	통과 (38.09ms, 10.2MB)
'''

#
# def solution(N, road, K):
#     answer = 0
#     unlink = int(5e5) + 1
#     time_table = [[unlink] * (N+1) for _ in range(N+1)]
#     for i in range(1, N+1):
#         time_table[i][i] = 0
#
#     for a, b, c in road:
#         if time_table[a][b] > c:
#             time_table[a][b] = c
#             time_table[b][a] = c
#     for via in range(1, N+1):
#         for start in range(1, N+1):
#             if via != start:
#                 for end in range(1, N+1):
#                     if via != end != start and time_table[start][via] != unlink != time_table[via][end]:
#                         time_table[start][end] = min(time_table[start][end], time_table[start][via] + time_table[via][end])
#
#
#     for i in range(1, N+1):
#         if time_table[1][i] <= K:
#             answer += 1
#     return answer
'''
테스트 1 〉	통과 (0.18ms, 10.1MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.07ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.32ms, 10.2MB)
테스트 6 〉	통과 (0.06ms, 10.2MB)
테스트 7 〉	통과 (0.09ms, 10.2MB)
테스트 8 〉	통과 (0.08ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.17ms, 10.1MB)
테스트 11 〉	통과 (0.25ms, 10.3MB)
테스트 12 〉	통과 (6.59ms, 10.3MB)
테스트 13 〉	통과 (8.00ms, 10.3MB)
테스트 14 〉	통과 (19.77ms, 10.2MB)
테스트 15 〉	통과 (23.63ms, 10.4MB)
테스트 16 〉	통과 (1.05ms, 10.3MB)
테스트 17 〉	통과 (5.79ms, 10.3MB)
테스트 18 〉	통과 (39.69ms, 10.2MB)
테스트 19 〉	통과 (44.17ms, 10.4MB)
테스트 20 〉	통과 (49.05ms, 10.2MB)
테스트 21 〉	통과 (36.63ms, 10.3MB)
테스트 22 〉	통과 (76.29ms, 10.2MB)
테스트 23 〉	통과 (59.61ms, 10.4MB)
테스트 24 〉	통과 (37.38ms, 10.3MB)
테스트 25 〉	통과 (49.68ms, 10.5MB)
테스트 26 〉	통과 (76.52ms, 10.5MB)
테스트 27 〉	통과 (64.50ms, 10.5MB)
테스트 28 〉	통과 (67.36ms, 10.7MB)
테스트 29 〉	통과 (72.05ms, 10.6MB)
테스트 30 〉	통과 (66.49ms, 10.4MB)
테스트 31 〉	통과 (44.26ms, 10.4MB)
테스트 32 〉	통과 (48.05ms, 10.2MB)
'''

#
#
# def solution(N, road, K):
#     answer = 0
#     unlink = K + 1
#     time_table = [[unlink] * (N+1) for _ in range(N+1)]
#     for i in range(1, N+1):
#         time_table[i][i] = 0
#
#     for a, b, c in road:
#         if time_table[a][b] > c:
#             time_table[a][b] = c
#             time_table[b][a] = c
#     for via in range(1, N+1):
#         for start in range(1, N+1):
#             if via != start:
#                 for end in range(1, N+1):
#                     if via != end != start:
#                         time_table[start][end] = min(time_table[start][end], time_table[start][via] + time_table[via][end])
#
#     for i in range(1, N+1):
#         if time_table[1][i] <= K:
#             answer += 1
#     return answer
'''
테스트 1 〉	통과 (0.17ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.06ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.1MB)
테스트 5 〉	통과 (0.45ms, 10.3MB)
테스트 6 〉	통과 (0.09ms, 10.4MB)
테스트 7 〉	통과 (0.06ms, 10.2MB)
테스트 8 〉	통과 (0.09ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.19ms, 10.1MB)
테스트 11 〉	통과 (0.27ms, 10.2MB)
테스트 12 〉	통과 (30.69ms, 10.3MB)
테스트 13 〉	통과 (8.80ms, 10.3MB)
테스트 14 〉	통과 (9.87ms, 10.4MB)
테스트 15 〉	통과 (18.34ms, 10.3MB)
테스트 16 〉	통과 (3.40ms, 10.2MB)
테스트 17 〉	통과 (12.33ms, 10.2MB)
테스트 18 〉	통과 (63.25ms, 10.3MB)
테스트 19 〉	통과 (32.78ms, 10.4MB)
테스트 20 〉	통과 (63.93ms, 10.3MB)
테스트 21 〉	통과 (27.21ms, 10.4MB)
테스트 22 〉	통과 (42.66ms, 10.3MB)
테스트 23 〉	통과 (48.93ms, 10.5MB)
테스트 24 〉	통과 (58.27ms, 10.3MB)
테스트 25 〉	통과 (58.17ms, 10.4MB)
테스트 26 〉	통과 (39.02ms, 10.4MB)
테스트 27 〉	통과 (49.06ms, 10.6MB)
테스트 28 〉	통과 (49.59ms, 10.4MB)
테스트 29 〉	통과 (49.30ms, 10.3MB)
테스트 30 〉	통과 (66.07ms, 10.4MB)
테스트 31 〉	통과 (50.94ms, 10.4MB)
테스트 32 〉	통과 (53.98ms, 10.4MB)
'''


#
def solution(N, road, K):
    answer = 0
    unlink = K + 1
    time_table = [[unlink] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        time_table[i][i] = 0

    for a, b, c in road:
        if time_table[a][b] > c:
            time_table[a][b] = c
            time_table[b][a] = c
    for via in range(1, N+1):
        for start in range(1, N):
            if via != start:
                for end in range(start, N+1):
                    new_time = time_table[start][via] + time_table[via][end]
                    if time_table[start][end] > new_time:
                        time_table[start][end] = new_time
                        time_table[end][start] = new_time


    for i in range(1, N+1):
        if time_table[1][i] <= K:
            answer += 1
    return answer
'''
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.04ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.16ms, 10.2MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
테스트 8 〉	통과 (0.05ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.13ms, 10.3MB)
테스트 11 〉	통과 (0.15ms, 10.3MB)
테스트 12 〉	통과 (6.56ms, 10.3MB)
테스트 13 〉	통과 (2.43ms, 10.2MB)
테스트 14 〉	통과 (2.39ms, 10.3MB)
테스트 15 〉	통과 (3.79ms, 10.3MB)
테스트 16 〉	통과 (0.77ms, 10.3MB)
테스트 17 〉	통과 (3.94ms, 10.2MB)
테스트 18 〉	통과 (19.45ms, 10.1MB)
테스트 19 〉	통과 (9.07ms, 10.4MB)
테스트 20 〉	통과 (15.30ms, 10.2MB)
테스트 21 〉	통과 (10.83ms, 10.4MB)
테스트 22 〉	통과 (15.49ms, 10.1MB)
테스트 23 〉	통과 (15.37ms, 10.4MB)
테스트 24 〉	통과 (12.03ms, 10.3MB)
테스트 25 〉	통과 (11.52ms, 10.5MB)
테스트 26 〉	통과 (10.02ms, 10.6MB)
테스트 27 〉	통과 (9.14ms, 10.5MB)
테스트 28 〉	통과 (15.02ms, 10.5MB)
테스트 29 〉	통과 (14.08ms, 10.6MB)
테스트 30 〉	통과 (11.60ms, 10.3MB)
테스트 31 〉	통과 (11.79ms, 10.3MB)
테스트 32 〉	통과 (15.19ms, 10.2MB)
'''
def solution(N, road, K):
    answer = 0
    unlink = K + 1
    time_table = [[unlink] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        time_table[i][i] = 0

    for a, b, c in road:
        if time_table[a][b] > c:
            time_table[a][b] = c
            time_table[b][a] = c
    for via in range(1, N+1):
        for start in range(1, N):
            if via != start:
                for end in range(start+1, N+1):
                    new_time = time_table[start][via] + time_table[via][end]
                    if time_table[start][end] > new_time:
                        time_table[start][end] = new_time
                        time_table[end][start] = new_time


    for i in range(1, N+1):
        if time_table[1][i] <= K:
            answer += 1
    return answer
'''
테스트 1 〉	통과 (0.06ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.09ms, 10.2MB)
테스트 6 〉	통과 (0.04ms, 10.3MB)
테스트 7 〉	통과 (0.03ms, 10.3MB)
테스트 8 〉	통과 (0.04ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.11ms, 10.2MB)
테스트 11 〉	통과 (0.10ms, 10.3MB)
테스트 12 〉	통과 (3.84ms, 10.4MB)
테스트 13 〉	통과 (2.95ms, 10.3MB)
테스트 14 〉	통과 (2.31ms, 10.4MB)
테스트 15 〉	통과 (4.11ms, 10.3MB)
테스트 16 〉	통과 (0.55ms, 10.3MB)
테스트 17 〉	통과 (2.10ms, 10.3MB)
테스트 18 〉	통과 (14.29ms, 10.2MB)
테스트 19 〉	통과 (11.36ms, 10.5MB)
테스트 20 〉	통과 (13.58ms, 10.3MB)
테스트 21 〉	통과 (10.88ms, 10.5MB)
테스트 22 〉	통과 (11.36ms, 10.2MB)
테스트 23 〉	통과 (9.47ms, 10.4MB)
테스트 24 〉	통과 (13.60ms, 10.3MB)
테스트 25 〉	통과 (11.69ms, 10.5MB)
테스트 26 〉	통과 (8.16ms, 10.4MB)
테스트 27 〉	통과 (12.66ms, 10.4MB)
테스트 28 〉	통과 (14.37ms, 10.7MB)
테스트 29 〉	통과 (15.86ms, 10.5MB)
테스트 30 〉	통과 (10.20ms, 10.4MB)
테스트 31 〉	통과 (8.76ms, 10.3MB)
테스트 32 〉	통과 (8.47ms, 10.3MB)
'''
def solution(N, road, K):
    answer = 0
    unlink = int(5e5) + 1
    time_table = [[unlink] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        time_table[i][i] = 0

    for a, b, c in road:
        if time_table[a][b] > c:
            time_table[a][b] = c
            time_table[b][a] = c
    for via in range(1, N+1):
        for start in range(1, N):
            if via != start:
                for end in range(start+1, N+1):
                    new_time = time_table[start][via] + time_table[via][end]
                    if time_table[start][end] > new_time:
                        time_table[start][end] = new_time
                        time_table[end][start] = new_time


    for i in range(1, N+1):
        if time_table[1][i] <= K:
            answer += 1
    return answer
'''
테스트 1 〉	통과 (0.04ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.04ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.4MB)
테스트 5 〉	통과 (0.09ms, 10.2MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.03ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.12ms, 10.2MB)
테스트 11 〉	통과 (0.09ms, 10.2MB)
테스트 12 〉	통과 (3.79ms, 10.3MB)
테스트 13 〉	통과 (2.32ms, 10.4MB)
테스트 14 〉	통과 (3.19ms, 10.4MB)
테스트 15 〉	통과 (8.95ms, 10.4MB)
테스트 16 〉	통과 (0.51ms, 10.3MB)
테스트 17 〉	통과 (1.71ms, 10.4MB)
테스트 18 〉	통과 (8.38ms, 10.4MB)
테스트 19 〉	통과 (7.48ms, 10.5MB)
테스트 20 〉	통과 (8.29ms, 10.2MB)
테스트 21 〉	통과 (6.21ms, 10.3MB)
테스트 22 〉	통과 (8.57ms, 10.2MB)
테스트 23 〉	통과 (8.96ms, 10.4MB)
테스트 24 〉	통과 (6.86ms, 10.2MB)
테스트 25 〉	통과 (9.28ms, 10.6MB)
테스트 26 〉	통과 (8.73ms, 10.5MB)
테스트 27 〉	통과 (7.30ms, 10.5MB)
테스트 28 〉	통과 (9.17ms, 10.6MB)
테스트 29 〉	통과 (9.28ms, 10.6MB)
테스트 30 〉	통과 (13.28ms, 10.5MB)
테스트 31 〉	통과 (8.62ms, 10.2MB)
테스트 32 〉	통과 (11.92ms, 10.2MB)
'''