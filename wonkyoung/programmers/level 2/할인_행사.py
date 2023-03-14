#230314
# def solution(want, number, discount):
#     length = len(discount)
#     cnt = len(want)
#     day = 0
#     items = {}
#     for i in range(9):
#         item = discount[i]
#         if items.get(item):
#             items[item] += 1
#         else:
#             items[item] = 1
#
#     for i in range(length-9):
#         item = discount[i+9]
#         if items.get(item):
#             items[item] += 1
#         else:
#             items[item] = 1
#
#         for j in range(cnt):
#             if items.get(want[j]):
#                 if items[want[j]] < number[j]:
#                     break
#             else:
#                 break
#         else:
#             day += 1
#
#         items[discount[i]] -= 1
#     return day
'''
정확성  테스트
테스트 1 〉	통과 (11.94ms, 10.6MB)
테스트 2 〉	통과 (79.84ms, 14.8MB)
테스트 3 〉	통과 (15.83ms, 11.1MB)
테스트 4 〉	통과 (59.67ms, 15.6MB)
테스트 5 〉	통과 (26.67ms, 13MB)
테스트 6 〉	통과 (4.45ms, 10.5MB)
테스트 7 〉	통과 (14.54ms, 11.2MB)
테스트 8 〉	통과 (62.73ms, 17.4MB)
테스트 9 〉	통과 (9.79ms, 11.2MB)
테스트 10 〉	통과 (32.56ms, 13.8MB)
테스트 11 〉	통과 (7.24ms, 10.6MB)
테스트 12 〉	통과 (0.01ms, 10.1MB)
'''

#
# def solution(want, number, discount):
#     length = len(discount)
#     cnt = len(want)
#     day = 0
#     items = {}
#     for i in range(9):
#         item = discount[i]
#         if items.get(item):
#             items[item] += 1
#         else:
#             items[item] = 1
#
#     for i in range(length-9):
#         item = discount[i+9]
#         if items.get(item):
#             items[item] += 1
#         else:
#             items[item] = 1
#
#         for j in range(cnt):
#             if not items.get(want[j]):
#                 break
#             elif items[want[j]] < number[j]:
#                 break
#         else:
#             day += 1
#
#         items[discount[i]] -= 1
#     return day
'''
정확성  테스트
테스트 1 〉	통과 (7.27ms, 10.6MB)
테스트 2 〉	통과 (52.12ms, 14.7MB)
테스트 3 〉	통과 (9.66ms, 11MB)
테스트 4 〉	통과 (86.71ms, 15.5MB)
테스트 5 〉	통과 (28.23ms, 12.8MB)
테스트 6 〉	통과 (8.17ms, 10.3MB)
테스트 7 〉	통과 (14.55ms, 11.5MB)
테스트 8 〉	통과 (56.47ms, 17.2MB)
테스트 9 〉	통과 (10.05ms, 11.2MB)
테스트 10 〉	통과 (55.70ms, 13.7MB)
테스트 11 〉	통과 (7.31ms, 10.5MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
'''

#
# def solution(want, number, discount):
#     length = len(discount)
#     cnt = len(want)
#     day = 0
#     items = {}
#     for i in range(9):
#         item = discount[i]
#         if items.get(item):
#             items[item] += 1
#         else:
#             items[item] = 1
#
#     for i in range(length-9):
#         item = discount[i+9]
#         if items.get(item):
#             items[item] += 1
#         else:
#             items[item] = 1
#
#         for j in range(cnt):
#             if not items.get(want[j]):
#                 break
#             elif items[want[j]] != number[j]:
#                 break
#         else:
#             day += 1
#
#         items[discount[i]] -= 1
#     return day
'''
정확성  테스트
테스트 1 〉	통과 (6.36ms, 10.6MB)
테스트 2 〉	통과 (57.39ms, 14.6MB)
테스트 3 〉	통과 (8.74ms, 11.2MB)
테스트 4 〉	통과 (56.46ms, 15.5MB)
테스트 5 〉	통과 (25.11ms, 13MB)
테스트 6 〉	통과 (7.98ms, 10.4MB)
테스트 7 〉	통과 (25.60ms, 11.3MB)
테스트 8 〉	통과 (61.39ms, 17.2MB)
테스트 9 〉	통과 (11.74ms, 11.2MB)
테스트 10 〉	통과 (38.70ms, 13.8MB)
테스트 11 〉	통과 (6.80ms, 10.5MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
'''

#
def solution(want, number, discount):
    length = len(discount)
    cnt = len(want)
    day = 0
    check = {want[i]:number[i] for i in range(cnt)}
    items = {}
    for i in range(9):
        item = discount[i]
        if items.get(item):
            items[item] += 1
        else:
            items[item] = 1

    for i in range(length-9):
        item = discount[i+9]
        if items.get(item):
            items[item] += 1
        else:
            items[item] = 1

        if check == items:
            day += 1

        items[discount[i]] -= 1
        if items[discount[i]] == 0:
            del items[discount[i]]
    return day
'''
정확성  테스트
테스트 1 〉	통과 (3.80ms, 10.7MB)
테스트 2 〉	통과 (26.08ms, 14.4MB)
테스트 3 〉	통과 (5.65ms, 11.2MB)
테스트 4 〉	통과 (27.76ms, 15.3MB)
테스트 5 〉	통과 (14.30ms, 12.9MB)
테스트 6 〉	통과 (2.56ms, 10.5MB)
테스트 7 〉	통과 (8.08ms, 11.5MB)
테스트 8 〉	통과 (35.25ms, 17.1MB)
테스트 9 〉	통과 (6.54ms, 11.1MB)
테스트 10 〉	통과 (20.85ms, 13.8MB)
테스트 11 〉	통과 (6.93ms, 10.7MB)
테스트 12 〉	통과 (0.01ms, 10MB)
'''