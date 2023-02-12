#230212
# def solution(array):
#     cnt = {}
#     keys = []
#     freq_val = []
#     freq_cnt = 0
#     for num in array:
#         if cnt.get(num):
#             cnt[num] += 1
#         else:
#             cnt[num] = 1
#             keys.append(num)
#     for key in keys:
#         value = cnt[key]
#         if value > freq_cnt:
#             freq_val = [key]
#             freq_cnt = value
#         elif value == freq_cnt:
#             freq_val.append(key)
#     if len(freq_val) == 1:
#         return freq_val[0]
#     return -1
'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.03ms, 10.1MB)
테스트 3 〉	통과 (0.04ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.00ms, 10.3MB)
테스트 7 〉	통과 (0.00ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.00ms, 10.1MB)
테스트 10 〉	통과 (0.00ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.1MB)
테스트 14 〉	통과 (0.02ms, 10.2MB)
테스트 15 〉	통과 (0.02ms, 10.1MB)
테스트 16 〉	통과 (0.01ms, 10.1MB)
'''
# def solution(array):
#     freq_val = []
#     freq_cnt = 0
#     length = len(array)
#     if length == 1:
#         return array[0]
#     array.sort()
#     now_val, now_cnt = array[0], 1
#     for i in range(1, length):
#         num = array[i]
#         if now_val == num:
#             now_cnt += 1
#         else:
#             if freq_cnt < now_cnt:
#                 freq_val = [now_val]
#                 freq_cnt = now_cnt
#             elif freq_cnt == now_cnt:
#                 freq_val.append(now_val)
#             now_val, now_cnt = num, 1
#     if freq_cnt < now_cnt:
#         freq_val = [now_val]
#     elif freq_cnt == now_cnt:
#         freq_val.append(now_val)
#     if len(freq_val) == 1:
#         return freq_val[0]
#     return -1
'''
테스트 1 〉	통과 (0.01ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.00ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
'''
def solution(array):
    from statistics import multimode
    freq_val = multimode(array)
    if len(freq_val) == 1:
        return freq_val[0]
    return -1
'''
테스트 1 〉	통과 (3.64ms, 11.1MB)
테스트 2 〉	통과 (19.55ms, 11.2MB)
테스트 3 〉	통과 (3.73ms, 11.3MB)
테스트 4 〉	통과 (21.07ms, 11.2MB)
테스트 5 〉	통과 (3.50ms, 11.2MB)
테스트 6 〉	통과 (3.52ms, 11.1MB)
테스트 7 〉	통과 (3.69ms, 11.1MB)
테스트 8 〉	통과 (3.48ms, 11.3MB)
테스트 9 〉	통과 (3.56ms, 11.1MB)
테스트 10 〉	통과 (3.80ms, 11.1MB)
테스트 11 〉	통과 (3.52ms, 11.2MB)
테스트 12 〉	통과 (3.86ms, 11.2MB)
테스트 13 〉	통과 (3.62ms, 11.1MB)
테스트 14 〉	통과 (3.84ms, 11.2MB)
테스트 15 〉	통과 (3.56ms, 11.1MB)
테스트 16 〉	통과 (3.47ms, 11.1MB)
'''