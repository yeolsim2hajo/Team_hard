# def solution(elements):
#     total_set = {sum(elements)}
#     for element in elements:
#         total_set.add(element)
#     length = len(elements)
#     elements += elements
#     ref = 0
#     for end in range(1, length-1):
#         ref += elements[end-1]
#         total = ref
#         for i in range(length):
#             total += elements[end+i]
#             total_set.add(total)
#             total -= elements[i]
#     return len(total_set)
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (8.29ms, 13.1MB)
테스트 3 〉	통과 (17.59ms, 14.2MB)
테스트 4 〉	통과 (34.59ms, 18.3MB)
테스트 5 〉	통과 (57.82ms, 26.9MB)
테스트 6 〉	통과 (86.35ms, 26.9MB)
테스트 7 〉	통과 (111.13ms, 26.9MB)
테스트 8 〉	통과 (118.56ms, 27.8MB)
테스트 9 〉	통과 (170.26ms, 43.7MB)
테스트 10 〉	통과 (200.57ms, 43.8MB)
테스트 11 〉	통과 (63.52ms, 26.9MB)
테스트 12 〉	통과 (72.38ms, 27MB)
테스트 13 〉	통과 (87.46ms, 26.9MB)
테스트 14 〉	통과 (96.68ms, 27MB)
테스트 15 〉	통과 (147.08ms, 27MB)
테스트 16 〉	통과 (143.86ms, 43.7MB)
테스트 17 〉	통과 (168.48ms, 43.6MB)
테스트 18 〉	통과 (188.12ms, 43.7MB)
테스트 19 〉	통과 (213.91ms, 43.5MB)
테스트 20 〉	통과 (304.12ms, 43.7MB)
'''


#
def solution(elements):
    total_set = {sum(elements)}
    length = len(elements)
    elements += elements
    for i in range(length):
        total = elements[i]
        total_set.add(total)
        for j in range(1, length-1):
            total += elements[i+j]
            total_set.add(total)
    return len(total_set)
'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (10.91ms, 13MB)
테스트 3 〉	통과 (14.97ms, 14.1MB)
테스트 4 〉	통과 (29.00ms, 18.4MB)
테스트 5 〉	통과 (59.67ms, 26.8MB)
테스트 6 〉	통과 (80.30ms, 27MB)
테스트 7 〉	통과 (117.69ms, 26.8MB)
테스트 8 〉	통과 (194.22ms, 27.7MB)
테스트 9 〉	통과 (212.13ms, 43.5MB)
테스트 10 〉	통과 (270.75ms, 43.7MB)
테스트 11 〉	통과 (79.26ms, 26.9MB)
테스트 12 〉	통과 (83.04ms, 26.8MB)
테스트 13 〉	통과 (92.88ms, 27MB)
테스트 14 〉	통과 (113.73ms, 27MB)
테스트 15 〉	통과 (142.99ms, 27MB)
테스트 16 〉	통과 (172.78ms, 43.7MB)
테스트 17 〉	통과 (210.99ms, 43.7MB)
테스트 18 〉	통과 (185.89ms, 43.6MB)
테스트 19 〉	통과 (252.17ms, 43.7MB)
테스트 20 〉	통과 (279.16ms, 43.7MB)
'''

print(solution([7,9,1,1,4]))