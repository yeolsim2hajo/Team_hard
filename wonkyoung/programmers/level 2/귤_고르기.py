#230307
# def solution(k, tangerine):
#     size_cnt = {}
#     total = 0
#     for size in tangerine:
#         total += 1
#         if size_cnt.get(size):
#             size_cnt[size] += 1
#         else:
#             size_cnt[size] = 1
#     keys = sorted(size_cnt, key=lambda key: size_cnt[key])
#     answer = len(keys)
#     if total > k:
#         for key in keys:
#             total -= size_cnt[key]
#             if total < k:
#                 return answer
#             if total == k:
#                 return answer - 1
#             answer -= 1
#     return answer
'''
테스트 1 〉	통과 (30.55ms, 13.2MB)
테스트 2 〉	통과 (16.59ms, 13.1MB)
테스트 3 〉	통과 (16.17ms, 13.2MB)
테스트 4 〉	통과 (24.30ms, 13.1MB)
테스트 5 〉	통과 (14.61ms, 10.8MB)
테스트 6 〉	통과 (15.30ms, 11.3MB)
테스트 7 〉	통과 (16.54ms, 12.4MB)
테스트 8 〉	통과 (15.39ms, 11.8MB)
테스트 9 〉	통과 (16.12ms, 11.6MB)
테스트 10 〉	통과 (16.97ms, 13MB)
테스트 11 〉	통과 (0.02ms, 10.1MB)
테스트 12 〉	통과 (0.01ms, 10.1MB)
테스트 13 〉	통과 (0.00ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 9.98MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.1MB)
테스트 19 〉	통과 (0.01ms, 10.2MB)
테스트 20 〉	통과 (0.01ms, 10.1MB)
테스트 21 〉	통과 (0.12ms, 9.97MB)
테스트 22 〉	통과 (0.52ms, 10.3MB)
테스트 23 〉	통과 (0.32ms, 10.3MB)
테스트 24 〉	통과 (0.34ms, 10.2MB)
테스트 25 〉	통과 (4.04ms, 11.1MB)
테스트 26 〉	통과 (6.85ms, 11.7MB)
테스트 27 〉	통과 (33.53ms, 21.8MB)
테스트 28 〉	통과 (30.18ms, 16.1MB)
테스트 29 〉	통과 (46.25ms, 17.8MB)
테스트 30 〉	통과 (43.52ms, 21.9MB)
테스트 31 〉	통과 (29.23ms, 12.3MB)
테스트 32 〉	통과 (19.78ms, 13.5MB)
테스트 33 〉	통과 (37.88ms, 18MB)
테스트 34 〉	통과 (35.66ms, 18MB)
'''

#
# def solution(k, tangerine):
#     size_cnt = {}
#     answer = total = 0
#     for size in tangerine:
#         total += 1
#         if size_cnt.get(size):
#             size_cnt[size] += 1
#         else:
#             answer += 1
#             size_cnt[size] = 1
#     values = sorted(size_cnt.values())
#     if total > k:
#         for value in values:
#             total -= value
#             if total < k:
#                 return answer
#             answer -= 1
#             if total == k:
#                 return answer
#     return answer
'''
테스트 1 〉	통과 (26.73ms, 13.2MB)
테스트 2 〉	통과 (16.15ms, 13.1MB)
테스트 3 〉	통과 (23.66ms, 13.5MB)
테스트 4 〉	통과 (25.27ms, 13.1MB)
테스트 5 〉	통과 (15.54ms, 11.1MB)
테스트 6 〉	통과 (15.46ms, 11.4MB)
테스트 7 〉	통과 (17.67ms, 12.5MB)
테스트 8 〉	통과 (15.72ms, 11.8MB)
테스트 9 〉	통과 (15.50ms, 11.6MB)
테스트 10 〉	통과 (16.69ms, 13MB)
테스트 11 〉	통과 (0.01ms, 10.4MB)
테스트 12 〉	통과 (0.00ms, 10.1MB)
테스트 13 〉	통과 (0.00ms, 10.2MB)
테스트 14 〉	통과 (0.00ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.00ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.3MB)
테스트 19 〉	통과 (0.01ms, 10.4MB)
테스트 20 〉	통과 (0.01ms, 10.3MB)
테스트 21 〉	통과 (0.10ms, 10.4MB)
테스트 22 〉	통과 (0.24ms, 10.4MB)
테스트 23 〉	통과 (0.26ms, 10.3MB)
테스트 24 〉	통과 (0.48ms, 10.2MB)
테스트 25 〉	통과 (3.55ms, 11.1MB)
테스트 26 〉	통과 (5.34ms, 11.8MB)
테스트 27 〉	통과 (23.58ms, 21.9MB)
테스트 28 〉	통과 (23.57ms, 16.3MB)
테스트 29 〉	통과 (29.33ms, 17.9MB)
테스트 30 〉	통과 (35.43ms, 21.8MB)
테스트 31 〉	통과 (25.66ms, 12.3MB)
테스트 32 〉	통과 (17.04ms, 13.7MB)
테스트 33 〉	통과 (28.89ms, 18.1MB)
테스트 34 〉	통과 (27.98ms, 18.1MB)
'''

#
def solution(k, tangerine):
    size_cnt = {}
    answer = 0
    for size in tangerine:
        if size_cnt.get(size):
            size_cnt[size] += 1
        else:
            size_cnt[size] = 1
    values = sorted(size_cnt.values(), reverse=True)
    cnt = 0
    for value in values:
        cnt += value
        answer += 1
        if cnt >= k:
            return answer
    return answer
'''
테스트 1 〉	통과 (13.64ms, 13.2MB)
테스트 2 〉	통과 (16.70ms, 13.2MB)
테스트 3 〉	통과 (13.59ms, 13.4MB)
테스트 4 〉	통과 (14.67ms, 13.1MB)
테스트 5 〉	통과 (11.72ms, 11.2MB)
테스트 6 〉	통과 (12.15ms, 11.3MB)
테스트 7 〉	통과 (13.66ms, 12.7MB)
테스트 8 〉	통과 (13.12ms, 11.9MB)
테스트 9 〉	통과 (12.48ms, 11.6MB)
테스트 10 〉	통과 (15.12ms, 12.8MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.00ms, 10.2MB)
테스트 13 〉	통과 (0.00ms, 10.2MB)
테스트 14 〉	통과 (0.00ms, 10.1MB)
테스트 15 〉	통과 (0.01ms, 10.1MB)
테스트 16 〉	통과 (0.00ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.1MB)
테스트 20 〉	통과 (0.01ms, 10.3MB)
테스트 21 〉	통과 (0.08ms, 10.2MB)
테스트 22 〉	통과 (0.16ms, 10.3MB)
테스트 23 〉	통과 (0.18ms, 10.3MB)
테스트 24 〉	통과 (0.17ms, 10.4MB)
테스트 25 〉	통과 (2.40ms, 11.1MB)
테스트 26 〉	통과 (3.35ms, 11.8MB)
테스트 27 〉	통과 (26.08ms, 21.9MB)
테스트 28 〉	통과 (22.54ms, 16.2MB)
테스트 29 〉	통과 (28.92ms, 18MB)
테스트 30 〉	통과 (26.64ms, 21.8MB)
테스트 31 〉	통과 (15.08ms, 12.3MB)
테스트 32 〉	통과 (14.56ms, 13.6MB)
테스트 33 〉	통과 (22.44ms, 18MB)
테스트 34 〉	통과 (24.17ms, 18.1MB)
'''