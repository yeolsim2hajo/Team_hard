#230220

# def solution(cacheSize, cities):
#     if cacheSize == 0:
#         return 5 * len(cities)
#     cacheCnt = 0
#     cache = {}
#     total_time = 0
#     for city in cities:
#         if cacheSize > cacheCnt:
#             cache[city] = cacheCnt
#         elif cache.get(city, -1) != -1:
#             total_time += 1
#         else:



#230224
# def solution(cache_size, cities):
#     if cache_size == 0:
#         return 5 * len(cities)
#     from collections import deque
#     total_time = 0
#     q, cache = deque(), set()
#     length = 0
#     is_full = False
#     for city in cities:
#         city = city.lower()
#         if city in cache:
#             q.remove(city)
#             q.append(city)
#             total_time += 1
#         else:
#             q.append(city)
#             cache.add(city)
#             total_time += 5
#             length += 1
#             if is_full:
#                 first = q.popleft()
#                 cache.remove(first)
#             elif length == cache_size:
#                 is_full = True
#
#     return total_time
'''
테스트 1 〉	통과 (0.02ms, 9.99MB)
테스트 2 〉	통과 (0.01ms, 10MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.00ms, 10.1MB)
테스트 7 〉	통과 (0.00ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.05ms, 10.2MB)
테스트 11 〉	통과 (69.80ms, 17.5MB)
테스트 12 〉	통과 (0.08ms, 10.1MB)
테스트 13 〉	통과 (0.08ms, 10.2MB)
테스트 14 〉	통과 (0.14ms, 10.1MB)
테스트 15 〉	통과 (0.25ms, 10.1MB)
테스트 16 〉	통과 (0.32ms, 10.1MB)
테스트 17 〉	통과 (0.00ms, 10.2MB)
테스트 18 〉	통과 (0.64ms, 10.1MB)
테스트 19 〉	통과 (0.63ms, 10.3MB)
테스트 20 〉	통과 (0.76ms, 10.3MB)
'''