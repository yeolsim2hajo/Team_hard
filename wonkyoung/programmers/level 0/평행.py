#230213
# def solution(dots):
#     remain_dots = [dot[:] for dot in dots]
#     for i in range(4):
#         x1, y1 = remain_dots.pop(i)
#         for j in range(3):
#             x2, y2 = remain_dots.pop(j)
#             slope1 = (x2-x1)/(y2-y1)
#             # print(remain_dots)
#             left, right = remain_dots
#             slope2 = (left[0] - right[0])/(left[1] - right[1])
#             if slope1 == slope2:
#                 return 1
#             remain_dots.insert(j, (x2, y2))
#         remain_dots.insert(i, (x1, y1))
#
#     return 0
# print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))
# print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))
'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10.4MB)
테스트 5 〉	통과 (0.01ms, 10.4MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.4MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
'''

#
# def solution(dots):
#     dots = [dot[:] for dot in dots]
#     for i in range(4):
#         x1, y1 = dots.pop(i)
#         for j in range(3):
#             x2, y2 = dots.pop(j)
#             slope1 = (x2-x1)/(y2-y1)
#             left, right = dots
#             slope2 = (left[0] - right[0])/(left[1] - right[1])
#             if slope1 == slope2:
#                 return 1
#             dots.insert(j, (x2, y2))
#         dots.insert(i, (x1, y1))
#
#     return 0
'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
'''
def solution(dots):
    dots = [dot[:] for dot in dots]
    for i in range(4):
        x1, y1 = dots.pop(i)
        for j in range(3):
            x2, y2 = dots.pop(j)
            left, right = dots
            slope = (left[0] - right[0])/(left[1] - right[1])
            if (x2-x1)/(y2-y1) == slope:
                return 1
            dots.insert(j, (x2, y2))
        dots.insert(i, (x1, y1))

    return 0
'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
'''