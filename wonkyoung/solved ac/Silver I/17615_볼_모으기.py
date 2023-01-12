#230112
# N = int(input())
# balls = list(map(str, input()))
# min_cnt = N
#
# def sort_balls(min_cnt, color, option=0):
#     if option == -1:
#         result = balls[::-1]
#     else:
#         result = balls[:]
#     cnt = conseq = 0
#     for i in range(N-1, -1, -1):
#         if result[i] == color:
#             conseq += 1
#         else:
#             for j in range(N - conseq):
#                 if result[j] == color:
#                     cnt += 1
#             return min(min_cnt, cnt)
#     return 0
#
# for color in ('R', 'B'):
#     first, last = balls[0], balls[-1]
#     if first == last:
#         min_cnt = min(sort_balls(min_cnt, color, -1), sort_balls(min_cnt, color))
#     elif first == color:
#         min_cnt = sort_balls(min_cnt, color, -1)
#     else:
#         min_cnt = sort_balls(min_cnt, color)
# print(min_cnt)


# conseq 없앰
# N = int(input())
# balls = list(map(str, input()))
# min_cnt = N
#
# def sort_balls(min_cnt, color, option=0):
#     if option == -1:
#         result = balls[::-1]
#     else:
#         result = balls[:]
#     cnt = 0
#     for i in range(N-1, -1, -1):
#         if result[i] != color:
#             for j in range(i+1):
#                 if result[j] == color:
#                     cnt += 1
#             return min(min_cnt, cnt)
#     return 0
#
# for color in ('R', 'B'):
#     first, last = balls[0], balls[-1]
#     if first == last:
#         min_cnt = min(sort_balls(min_cnt, color, -1), sort_balls(min_cnt, color))
#     elif first == color:
#         min_cnt = sort_balls(min_cnt, color, -1)
#     else:
#         min_cnt = sort_balls(min_cnt, color)
# print(min_cnt)


# list X
# N = int(input())
# balls = input()
# min_cnt = N
#
# def sort_balls(min_cnt, color, option=0):
#     if option == -1:
#         result = balls[::-1]
#     else:
#         result = balls[:]
#     cnt = 0
#     for i in range(N-1, -1, -1):
#         if result[i] != color:
#             for j in range(i+1):
#                 if result[j] == color:
#                     cnt += 1
#             return min(min_cnt, cnt)
#     return 0
#
# for color in ('R', 'B'):
#     first, last = balls[0], balls[-1]
#     if first == last:
#         min_cnt = min(sort_balls(min_cnt, color, -1), sort_balls(min_cnt, color))
#     elif first == color:
#         min_cnt = sort_balls(min_cnt, color, -1)
#     else:
#         min_cnt = sort_balls(min_cnt, color)
# print(min_cnt)

# global
# N = int(input())
# balls = input()
# min_cnt = N
#
# def sort_balls(color, option=0):
#     global min_cnt
#     if option == -1:
#         result = balls[::-1]
#     else:
#         result = balls[:]
#     cnt = 0
#     for i in range(N-1, -1, -1):
#         if result[i] != color:
#             for j in range(i+1):
#                 if result[j] == color:
#                     cnt += 1
#             if cnt < min_cnt:
#                 min_cnt = cnt
#             return
#     min_cnt = 0
#
# for color in ('R', 'B'):
#     first, last = balls[0], balls[-1]
#     if first == last:
#         sort_balls(color, -1)
#         sort_balls(color)
#     elif first == color:
#         sort_balls(color, -1)
#     else:
#         sort_balls(color)
# print(min_cnt)


# 함수화
# def find_cnt():
#     N = int(input())
#     balls = input()
#     min_cnt = N
#
#     def sort_balls(color, option=0):
#         nonlocal min_cnt
#         if option == -1:
#             result = balls[::-1]
#         else:
#             result = balls[:]
#         cnt = 0
#         for i in range(N-1, -1, -1):
#             if result[i] != color:
#                 for j in range(i+1):
#                     if result[j] == color:
#                         cnt += 1
#                 if cnt < min_cnt:
#                     min_cnt = cnt
#                 return
#         min_cnt = 0
#
#     for color in ('R', 'B'):
#         first, last = balls[0], balls[-1]
#         if first == last:
#             sort_balls(color, -1)
#             sort_balls(color)
#         elif first == color:
#             sort_balls(color, -1)
#         else:
#             sort_balls(color)
#     return min_cnt
#
# print(find_cnt())


# 인자
# def find_cnt(N, balls):
#     min_cnt = N
#
#     def sort_balls(color, option=0):
#         nonlocal min_cnt
#         if option == -1:
#             result = balls[::-1]
#         else:
#             result = balls[:]
#         cnt = 0
#         for i in range(N-1, -1, -1):
#             if result[i] != color:
#                 for j in range(i+1):
#                     if result[j] == color:
#                         cnt += 1
#                 if cnt < min_cnt:
#                     min_cnt = cnt
#                 return
#         min_cnt = 0
#
#     for color in ('R', 'B'):
#         first, last = balls[0], balls[-1]
#         if first == last:
#             sort_balls(color, -1)
#             sort_balls(color)
#         elif first == color:
#             sort_balls(color, -1)
#         else:
#             sort_balls(color)
#     return min_cnt
#
# N = int(input())
# balls = input()
# print(find_cnt(N, balls))

# color 삭제
def find_cnt(N, balls):
    min_cnt = N

    def sort_balls(option=0):
        nonlocal min_cnt
        if option == -1:
            result = balls[::-1]
        else:
            result = balls[:]
        cnt = 0
        for i in range(N-1, -1, -1):
            if result[i] != color:
                for j in range(i+1):
                    if result[j] == color:
                        cnt += 1
                if cnt < min_cnt:
                    min_cnt = cnt
                return
        min_cnt = 0

    for color in ('R', 'B'):
        first, last = balls[0], balls[-1]
        if first == last:
            sort_balls(-1)
            sort_balls()
        elif first == color:
            sort_balls(-1)
        else:
            sort_balls()
    return min_cnt

N = int(input())
balls = input()
print(find_cnt(N, balls))