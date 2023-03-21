#230321
# def solution(land):
#     length = len(land)
#     for i in range(length-1):
#         row = land[i]
#         max_val = max(row)
#         for j in range(4):
#             if row[j] != max_val:
#                 land[i+1][j] += max_val
#             else:
#                 second_max_val = max(row[:j]+row[j+1:])
#                 land[i+1][j] += second_max_val
#
#     return max(land[-1])
'''
정확성  테스트
테스트 1 〉	통과 (1.33ms, 10.2MB)
테스트 2 〉	통과 (1.52ms, 10.4MB)
테스트 3 〉	통과 (1.38ms, 10.2MB)
테스트 4 〉	통과 (2.36ms, 10.3MB)
테스트 5 〉	통과 (1.45ms, 10.4MB)
테스트 6 〉	통과 (1.31ms, 10.5MB)
테스트 7 〉	통과 (1.36ms, 10.1MB)
테스트 8 〉	통과 (1.35ms, 10.3MB)
테스트 9 〉	통과 (1.29ms, 10.3MB)
테스트 10 〉	통과 (1.31ms, 10.5MB)
테스트 11 〉	통과 (1.29ms, 10.4MB)
테스트 12 〉	통과 (1.37ms, 10.3MB)
테스트 13 〉	통과 (2.69ms, 10.3MB)
테스트 14 〉	통과 (2.43ms, 10.3MB)
테스트 15 〉	통과 (1.53ms, 10.3MB)
테스트 16 〉	통과 (1.34ms, 10.3MB)
테스트 17 〉	통과 (1.50ms, 10.4MB)
테스트 18 〉	통과 (1.39ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (139.67ms, 32.3MB)
테스트 2 〉	통과 (138.71ms, 32.4MB)
테스트 3 〉	통과 (122.21ms, 32.4MB)
테스트 4 〉	통과 (137.87ms, 32.3MB)
'''


#
# def solution(land):
#     length = len(land)
#     for i in range(length-1):
#         row = land[i]
#         sorted_row = sorted(land[i])
#         max_val = sorted_row[-1]
#         for j in range(4):
#             if row[j] != max_val:
#                 land[i+1][j] += max_val
#             else:
#                 land[i+1][j] += sorted_row[-2]
#
#     return max(land[-1])
'''
정확성  테스트
테스트 1 〉	통과 (1.03ms, 10.3MB)
테스트 2 〉	통과 (1.75ms, 10.3MB)
테스트 3 〉	통과 (1.04ms, 10.4MB)
테스트 4 〉	통과 (1.07ms, 10.3MB)
테스트 5 〉	통과 (1.08ms, 10.5MB)
테스트 6 〉	통과 (1.24ms, 10.4MB)
테스트 7 〉	통과 (1.29ms, 10.4MB)
테스트 8 〉	통과 (1.49ms, 10.3MB)
테스트 9 〉	통과 (2.04ms, 10.3MB)
테스트 10 〉	통과 (1.77ms, 10.6MB)
테스트 11 〉	통과 (1.07ms, 10.4MB)
테스트 12 〉	통과 (1.07ms, 10.3MB)
테스트 13 〉	통과 (1.07ms, 10.1MB)
테스트 14 〉	통과 (1.14ms, 10.3MB)
테스트 15 〉	통과 (1.10ms, 10.2MB)
테스트 16 〉	통과 (1.29ms, 10.3MB)
테스트 17 〉	통과 (1.28ms, 10.3MB)
테스트 18 〉	통과 (1.14ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (108.98ms, 32.3MB)
테스트 2 〉	통과 (110.80ms, 32.4MB)
테스트 3 〉	통과 (98.71ms, 32.5MB)
테스트 4 〉	통과 (98.62ms, 32.4MB)
'''

#
def solution(land):
    length = len(land)
    for i in range(length-1):
        row = land[i]
        sorted_row = list(enumerate(row))
        sorted_row.sort(key=lambda x:x[1])
        max_j, max_val = sorted_row[-1]
        for j in range(4):
            if j != max_j:
                land[i+1][j] += max_val
            else:
                land[i+1][j] += sorted_row[-2][1]

    return max(land[-1])
'''
정확성  테스트
테스트 1 〉	통과 (3.34ms, 10.5MB)
테스트 2 〉	통과 (2.97ms, 10.5MB)
테스트 3 〉	통과 (3.28ms, 10.3MB)
테스트 4 〉	통과 (2.93ms, 10.4MB)
테스트 5 〉	통과 (2.18ms, 10.4MB)
테스트 6 〉	통과 (1.80ms, 10.6MB)
테스트 7 〉	통과 (2.08ms, 10.4MB)
테스트 8 〉	통과 (2.40ms, 10.3MB)
테스트 9 〉	통과 (3.78ms, 10.5MB)
테스트 10 〉	통과 (2.44ms, 10.3MB)
테스트 11 〉	통과 (2.86ms, 10.3MB)
테스트 12 〉	통과 (3.11ms, 10.4MB)
테스트 13 〉	통과 (2.84ms, 10.3MB)
테스트 14 〉	통과 (3.12ms, 10.5MB)
테스트 15 〉	통과 (3.11ms, 10.2MB)
테스트 16 〉	통과 (3.05ms, 10.4MB)
테스트 17 〉	통과 (2.05ms, 10.4MB)
테스트 18 〉	통과 (3.26ms, 10.5MB)
효율성  테스트
테스트 1 〉	통과 (162.75ms, 32.5MB)
테스트 2 〉	통과 (163.92ms, 32.4MB)
테스트 3 〉	통과 (149.23ms, 32.4MB)
테스트 4 〉	통과 (162.91ms, 32.4MB)
'''