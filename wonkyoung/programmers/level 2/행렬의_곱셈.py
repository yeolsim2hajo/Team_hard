#230208
# zip, map
# def solution(arr1, arr2):
#     row_one, row_two = len(arr1), len(arr2[0])
#     answer = [[] for _ in range(row_one)]
#     arr2 = list(zip(*arr2))
#     multiple = lambda x, y: x * y
#     for i in range(row_one):
#         for j in range(row_two):
#             answer[i].append(sum(map(multiple, arr1[i][:], arr2[j][:])))
#     return answer
'''
테스트 1 〉	통과 (3.88ms, 10.3MB)
테스트 2 〉	통과 (42.55ms, 11MB)
테스트 3 〉	통과 (51.11ms, 11.2MB)
테스트 4 〉	통과 (1.77ms, 10.3MB)
테스트 5 〉	통과 (30.22ms, 10.8MB)
테스트 6 〉	통과 (33.02ms, 10.9MB)
테스트 7 〉	통과 (1.69ms, 10.2MB)
테스트 8 〉	통과 (0.43ms, 10.2MB)
테스트 9 〉	통과 (0.36ms, 10.3MB)
테스트 10 〉	통과 (30.28ms, 10.6MB)
테스트 11 〉	통과 (3.38ms, 10.3MB)
테스트 12 〉	통과 (0.72ms, 10.3MB)
테스트 13 〉	통과 (27.73ms, 10.7MB)
테스트 14 〉	통과 (45.55ms, 10.9MB)
테스트 15 〉	통과 (13.63ms, 10.3MB)
테스트 16 〉	통과 (4.76ms, 10.6MB)
'''


#
# def solution(arr1, arr2):
#     row_one, col_one, row_two = len(arr1), len(arr1[0]) ,len(arr2[0])
#     answer = [[] for _ in range(row_one)]
#     arr2 = list(zip(*arr2))
#     multiple = lambda x, y: x * y
#     for i in range(row_one):
#         for j in range(row_two):
#             total = 0
#             for k in range(col_one):
#                 total += multiple(arr1[i][k], arr2[j][k])
#             answer[i].append(total)
#     return answer
'''
테스트 1 〉	통과 (4.03ms, 10.3MB)
테스트 2 〉	통과 (80.91ms, 11MB)
테스트 3 〉	통과 (87.67ms, 11.2MB)
테스트 4 〉	통과 (1.78ms, 10.4MB)
테스트 5 〉	통과 (58.68ms, 10.8MB)
테스트 6 〉	통과 (33.40ms, 10.9MB)
테스트 7 〉	통과 (1.70ms, 10.2MB)
테스트 8 〉	통과 (0.70ms, 10.4MB)
테스트 9 〉	통과 (0.53ms, 10.2MB)
테스트 10 〉	통과 (60.85ms, 10.7MB)
테스트 11 〉	통과 (5.46ms, 10.3MB)
테스트 12 〉	통과 (0.87ms, 10.3MB)
테스트 13 〉	통과 (43.82ms, 10.7MB)
테스트 14 〉	통과 (90.20ms, 11MB)
테스트 15 〉	통과 (28.30ms, 10.4MB)
테스트 16 〉	통과 (8.37ms, 10.5MB)
'''

# def solution(arr1, arr2):
#     row_one, col_one, row_two = len(arr1), len(arr1[0]) ,len(arr2[0])
#     answer = [[] for _ in range(row_one)]
#     arr2 = list(zip(*arr2))
#     for i in range(row_one):
#         for j in range(row_two):
#             total = 0
#             for k in range(col_one):
#                 total += arr1[i][k] * arr2[j][k]
#             answer[i].append(total)
#     return answer
'''
테스트 1 〉	통과 (2.80ms, 10.5MB)
테스트 2 〉	통과 (56.18ms, 11MB)
테스트 3 〉	통과 (60.46ms, 11.2MB)
테스트 4 〉	통과 (1.35ms, 10.2MB)
테스트 5 〉	통과 (44.25ms, 10.9MB)
테스트 6 〉	통과 (24.16ms, 10.9MB)
테스트 7 〉	통과 (1.23ms, 10.4MB)
테스트 8 〉	통과 (0.50ms, 10.3MB)
테스트 9 〉	통과 (0.40ms, 10.2MB)
테스트 10 〉	통과 (40.97ms, 10.6MB)
테스트 11 〉	통과 (4.26ms, 10.4MB)
테스트 12 〉	통과 (0.66ms, 10.2MB)
테스트 13 〉	통과 (29.92ms, 10.8MB)
테스트 14 〉	통과 (83.37ms, 11MB)
테스트 15 〉	통과 (29.20ms, 10.3MB)
테스트 16 〉	통과 (5.76ms, 10.6MB)
'''

# def solution(arr1, arr2):
#     row_one, col_one, row_two = len(arr1), len(arr1[0]) ,len(arr2[0])
#     answer = [[] for _ in range(row_one)]
#     for i in range(row_one):
#         for j in range(row_two):
#             total = 0
#             for k in range(col_one):
#                 total += arr1[i][k] * arr2[k][j]
#             answer[i].append(total)
#     return answer
'''
테스트 1 〉	통과 (2.81ms, 10.3MB)
테스트 2 〉	통과 (56.61ms, 11MB)
테스트 3 〉	통과 (61.53ms, 11.2MB)
테스트 4 〉	통과 (1.23ms, 10.1MB)
테스트 5 〉	통과 (42.83ms, 10.9MB)
테스트 6 〉	통과 (23.38ms, 11MB)
테스트 7 〉	통과 (1.15ms, 10.2MB)
테스트 8 〉	통과 (0.50ms, 10.2MB)
테스트 9 〉	통과 (0.39ms, 10.2MB)
테스트 10 〉	통과 (42.35ms, 10.7MB)
테스트 11 〉	통과 (3.83ms, 10.5MB)
테스트 12 〉	통과 (0.66ms, 10.4MB)
테스트 13 〉	통과 (52.37ms, 10.7MB)
테스트 14 〉	통과 (75.48ms, 10.8MB)
테스트 15 〉	통과 (19.20ms, 10.5MB)
테스트 16 〉	통과 (5.81ms, 10.5MB)
'''

# def solution(arr1, arr2):
#     row_one, col_one, row_two = len(arr1), len(arr1[0]) ,len(arr2[0])
#     answer = [[] for _ in range(row_one)]
#     arr2 = list(zip(*arr2))
#     for i in range(row_one):
#         left = arr1[i]
#         for j in range(row_two):
#             right = arr2[j]
#             total = 0
#             for k in range(col_one):
#                 total += left[k] * right[k]
#             answer[i].append(total)
#     return answer
'''
테스트 1 〉	통과 (2.10ms, 10.3MB)
테스트 2 〉	통과 (51.11ms, 10.8MB)
테스트 3 〉	통과 (54.49ms, 11.1MB)
테스트 4 〉	통과 (0.93ms, 10.3MB)
테스트 5 〉	통과 (30.92ms, 10.8MB)
테스트 6 〉	통과 (18.00ms, 10.9MB)
테스트 7 〉	통과 (0.90ms, 10.3MB)
테스트 8 〉	통과 (0.41ms, 10.3MB)
테스트 9 〉	통과 (0.33ms, 10.3MB)
테스트 10 〉	통과 (31.07ms, 10.6MB)
테스트 11 〉	통과 (3.08ms, 10.4MB)
테스트 12 〉	통과 (0.58ms, 10.3MB)
테스트 13 〉	통과 (22.91ms, 10.7MB)
테스트 14 〉	통과 (59.09ms, 11MB)
테스트 15 〉	통과 (14.39ms, 10.7MB)
테스트 16 〉	통과 (4.46ms, 10.5MB)
'''

def solution(arr1, arr2):
    row_one, row_two = len(arr1), len(arr2[0])
    answer = [[] for _ in range(row_one)]
    arr2 = list(zip(*arr2))
    multiple = lambda x, y: x * y
    for i in range(row_one):
        left = arr1[i]
        for j in range(row_two):
            answer[i].append(sum(map(multiple, left, arr2[j])))
    return answer
'''
테스트 1 〉	통과 (3.56ms, 10.4MB)
테스트 2 〉	통과 (39.40ms, 11MB)
테스트 3 〉	통과 (47.30ms, 11.2MB)
테스트 4 〉	통과 (0.94ms, 10.2MB)
테스트 5 〉	통과 (32.06ms, 10.9MB)
테스트 6 〉	통과 (17.56ms, 10.8MB)
테스트 7 〉	통과 (0.86ms, 10.2MB)
테스트 8 〉	통과 (0.42ms, 10.2MB)
테스트 9 〉	통과 (0.46ms, 10.3MB)
테스트 10 〉	통과 (50.56ms, 10.7MB)
테스트 11 〉	통과 (5.70ms, 10.4MB)
테스트 12 〉	통과 (0.60ms, 10.2MB)
테스트 13 〉	통과 (21.54ms, 10.8MB)
테스트 14 〉	통과 (43.75ms, 10.9MB)
테스트 15 〉	통과 (13.22ms, 10.4MB)
테스트 16 〉	통과 (8.22ms, 10.6MB)
'''
