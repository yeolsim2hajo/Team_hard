#230222
# def solution(lines):
#     min_start, max_end = 100, -100
#     for start, end in lines:
#         if start < min_start:
#             min_start = start
#         if end > max_end:
#             max_end = end
#     check = [0] * (max_end - min_start + 1)
#
#     value = 1
#     for start, end in lines:
#         for i in range(start - min_start, end - min_start+1):
#             check[i] += value
#         value += 2
#
#     total = 0
#     start = -1
#     for i in range(max_end - min_start + 1):
#         if start == -1:
#             if check[i] not in {0, 1, 3, 5}:
#                 start = i
#         elif check[i] in {0, 1, 3, 5}:
#             total += i - start - 1
#             start = -1
#
#     return total


#230304
def solution(lines):
    total_set = set()
    lines.append(lines[0])
    set1 = set(range(lines[0][0], lines[0][1]))
    for i in range(1, 4):
        start, end = lines[i]
        set2 = set(range(start, end))
        total_set.update(set1 & set2)
        set1 = set(set2)
    return len(total_set)
'''
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.05ms, 10.4MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.4MB)
'''

