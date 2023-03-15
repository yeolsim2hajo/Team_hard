#230307
# 실패
# def solution(people, limit):
#     answer = 0
#     people.sort()
#     length = len(people)
#     def find_lighter(weight, limit):
#         start, end = 0, limit
#         while start <= end:
#             mid = (start + end) // 2
#             if people[mid] > weight:
#                 end = mid - 1
#             elif people[mid] < weight:
#                 start = mid + 1
#             else:
#                 return mid
#         return end
#     while people:
#         heavier = people.pop()
#         length -= 1
#         remain = limit - heavier
#         index = find_lighter(remain, length-1)
#         if index >= 0:
#             while remain:
#                 remain -= people.pop(index)
#                 length -= 1
#                 index = find_lighter(remain, length - 1)
#                 if index < 0:
#                     break
#         answer += 1
#     return answer


#230315
# def solution(people, limit):
#     answer = 0
#     people.sort()
#     length = len(people)
#     start, end = 0, length-1
#     lighter, heavier = people[start], people[end]
#     while start <= end:
#         if lighter + heavier <= limit:
#             start += 1
#             lighter = people[start]
#         end -= 1
#         heavier = people[end]
#         answer += 1
#     return answer
'''
정확성  테스트
테스트 1 〉	통과 (1.17ms, 10.2MB)
테스트 2 〉	통과 (0.91ms, 10.2MB)
테스트 3 〉	통과 (0.56ms, 10.4MB)
테스트 4 〉	통과 (0.50ms, 10.2MB)
테스트 5 〉	통과 (0.30ms, 10.1MB)
테스트 6 〉	통과 (0.18ms, 10.3MB)
테스트 7 〉	통과 (0.28ms, 10.2MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.07ms, 10.1MB)
테스트 10 〉	통과 (0.52ms, 10.1MB)
테스트 11 〉	통과 (0.45ms, 10.2MB)
테스트 12 〉	통과 (0.42ms, 10.2MB)
테스트 13 〉	통과 (0.73ms, 10.2MB)
테스트 14 〉	통과 (0.82ms, 10.2MB)
테스트 15 〉	통과 (0.06ms, 9.97MB)
효율성  테스트
테스트 1 〉	통과 (7.65ms, 10.6MB)
테스트 2 〉	통과 (9.27ms, 10.5MB)
테스트 3 〉	통과 (8.08ms, 10.5MB)
테스트 4 〉	통과 (9.39ms, 10.6MB)
테스트 5 〉	통과 (7.93ms, 10.5MB)
'''


#
def solution(people, limit):
    answer = 0
    people.sort()
    length = len(people)
    start, end = 0, length-1
    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
        answer += 1
    return answer
'''
정확성  테스트
테스트 1 〉	통과 (1.40ms, 10.3MB)
테스트 2 〉	통과 (1.02ms, 10.3MB)
테스트 3 〉	통과 (0.81ms, 10.2MB)
테스트 4 〉	통과 (0.83ms, 10.1MB)
테스트 5 〉	통과 (0.43ms, 10.1MB)
테스트 6 〉	통과 (0.28ms, 10.1MB)
테스트 7 〉	통과 (0.28ms, 10.1MB)
테스트 8 〉	통과 (0.05ms, 10.2MB)
테스트 9 〉	통과 (0.05ms, 10.2MB)
테스트 10 〉	통과 (0.55ms, 10.1MB)
테스트 11 〉	통과 (0.45ms, 10.2MB)
테스트 12 〉	통과 (0.45ms, 10.3MB)
테스트 13 〉	통과 (0.57ms, 10.3MB)
테스트 14 〉	통과 (0.75ms, 10MB)
테스트 15 〉	통과 (0.06ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (8.58ms, 10.5MB)
테스트 2 〉	통과 (9.32ms, 10.5MB)
테스트 3 〉	통과 (8.22ms, 10.6MB)
테스트 4 〉	통과 (9.19ms, 10.5MB)
테스트 5 〉	통과 (8.32ms, 10.5MB)
'''