#230105
# 시간초과
# def solution(number, limit, power):
#     answer = 1
#     for i in range(2, number+1):
#         cnt = 2
#         for j in range(2, i//2+1):
#             if i%j == 0:
#                 cnt += 1
#         if cnt > limit:
#             cnt = power
#         answer += cnt
#     return answer


# 제곱근
# def solution(number, limit, power):
#     from math import isqrt
#     answer = 1
#     for i in range(2, number+1):
#         cnt = 2
#         end = isqrt(i)
#         for j in range(2, end+1):
#             if i%j == 0:
#                 cnt += 2
#         if end ** 2 == i:
#             cnt -= 1
#         if cnt > limit:
#             cnt = power
#         answer += cnt
#     return answer
'''
테스트 1 〉	통과 (42.61ms, 10.3MB)
테스트 2 〉	통과 (4.64ms, 10.2MB)
테스트 3 〉	통과 (3.16ms, 10.2MB)
테스트 4 〉	통과 (11.10ms, 10.1MB)
테스트 5 〉	통과 (2.42ms, 10.2MB)
테스트 6 〉	통과 (36.71ms, 10.2MB)
테스트 7 〉	통과 (4.57ms, 10MB)
테스트 8 〉	통과 (5.13ms, 10.3MB)
테스트 9 〉	통과 (52.25ms, 10.1MB)
테스트 10 〉	통과 (3.11ms, 10.2MB)
테스트 11 〉	통과 (750.87ms, 10.2MB)
테스트 12 〉	통과 (761.01ms, 10.2MB)
테스트 13 〉	통과 (776.11ms, 10.3MB)
테스트 14 〉	통과 (815.05ms, 10.1MB)
테스트 15 〉	통과 (847.83ms, 9.98MB)
테스트 16 〉	통과 (831.34ms, 10.1MB)
테스트 17 〉	통과 (0.00ms, 10.2MB)
테스트 18 〉	통과 (1038.54ms, 10.2MB)
테스트 19 〉	통과 (7.80ms, 10.2MB)
테스트 20 〉	통과 (7.58ms, 10.1MB)
테스트 21 〉	통과 (0.01ms, 9.99MB)
테스트 22 〉	통과 (0.01ms, 10.3MB)
테스트 23 〉	통과 (0.01ms, 10.1MB)
테스트 24 〉	통과 (814.59ms, 10.3MB)
테스트 25 〉	통과 (822.11ms, 10.2MB)
테스트 26 〉	통과 (1.16ms, 10.1MB)
테스트 27 〉	통과 (1.11ms, 10.2MB)
'''


# isqrt 사용 X
# def solution(number, limit, power):
#     answer = 1
#     for i in range(2, number+1):
#         cnt, end = 2, 1
#         for j in range(1, i):
#             square = j**2
#             if square >= i:
#                 end = j
#                 if square == i:
#                     cnt += 1
#                 break
#         for j in range(2, end):
#             if i%j == 0:
#                 cnt += 2
#         if cnt > limit:
#             cnt = power
#         answer += cnt
#     return answer
'''
테스트 1 〉	통과 (160.58ms, 10.2MB)
테스트 2 〉	통과 (21.76ms, 10.2MB)
테스트 3 〉	통과 (9.31ms, 10.2MB)
테스트 4 〉	통과 (43.57ms, 10.3MB)
테스트 5 〉	통과 (5.17ms, 10.2MB)
테스트 6 〉	통과 (169.60ms, 10.2MB)
테스트 7 〉	통과 (36.73ms, 10.2MB)
테스트 8 〉	통과 (12.50ms, 10.1MB)
테스트 9 〉	통과 (156.72ms, 10.2MB)
테스트 10 〉	통과 (7.97ms, 10.2MB)
테스트 11 〉	통과 (4764.26ms, 10MB)
테스트 12 〉	통과 (4754.39ms, 10.3MB)
테스트 13 〉	통과 (5486.16ms, 10.2MB)
테스트 14 〉	통과 (5646.10ms, 10.2MB)
테스트 15 〉	통과 (6220.31ms, 10MB)
테스트 16 〉	통과 (6339.68ms, 10.3MB)
테스트 17 〉	통과 (0.00ms, 10.1MB)
테스트 18 〉	통과 (6386.18ms, 10.1MB)
테스트 19 〉	통과 (24.95ms, 10.2MB)
테스트 20 〉	통과 (25.37ms, 10MB)
테스트 21 〉	통과 (0.01ms, 10MB)
테스트 22 〉	통과 (0.01ms, 10.1MB)
테스트 23 〉	통과 (0.02ms, 10.2MB)
테스트 24 〉	통과 (5426.44ms, 10.2MB)
테스트 25 〉	통과 (5534.89ms, 10MB)
테스트 26 〉	통과 (4.49ms, 10.2MB)
테스트 27 〉	통과 (4.64ms, 10.2MB)
'''