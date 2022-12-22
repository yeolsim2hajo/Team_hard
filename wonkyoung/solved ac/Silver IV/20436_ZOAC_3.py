#220929 (Type Error)
# left = {'q', 'w', 'e', 'r', 't', 'a', 's',
#         'd', 'f', 'g', 'z', 'x', 'c', 'v'}
# keyboard = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
#             ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
#             ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
# width = [10, 9, 7]
# left_finger, right_finger = input().split()
# word = input()
#
# def find_position(finger, position):
#     for i in range(3):
#         half = (width[i]+1)//2
#         start, end = half * position, width[i] - half * (1 - position)
#         for j in range(start, end):
#             if finger == keyboard[i][j]:
#                 return (i, j)
#
# left_now = find_position(left_finger, 0)
# right_now = find_position(right_finger, 1)
#
# min_time = 0
# for alp in word:
#     min_time += 1
#     if alp in left:
#         new_left = find_position(alp, 0)
#         for i in range(2):
#             min_time += abs(new_left[i] - left_now[i])
#         left_now = new_left
#     else:
#         new_right = find_position(alp, 1)
#         for i in range(2):
#             min_time += abs(new_right[i] - right_now[i])
#         right_now = new_right
# print(min_time)


#221222
# left = {'q', 'w', 'e', 'r', 't',
#         'a', 's', 'd', 'f', 'g',
#         'z', 'x', 'c', 'v'}
# keyboard = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
#             ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
#             ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
# match = {}
# for i in range(3):
#     for j in range(len(keyboard[i])):
#         alp = keyboard[i][j]
#         match[alp] = (i, j)
#
# def return_position(alp):
#     return match[alp]
#
# left_position, right_position = map(return_position,input().split())
# word = input()
# cnt = 0
# for alp in word:
#     nx, ny = return_position(alp)
#     if alp in left:
#         x, y = left_position
#         left_position = (nx, ny)
#     else:
#         x, y = right_position
#         right_position = (nx, ny)
#     cnt += abs(nx - x) + abs(ny - y) + 1
# print(cnt)


# 함수로
# def find_cnt():
#     left = {'q', 'w', 'e', 'r', 't',
#             'a', 's', 'd', 'f', 'g',
#             'z', 'x', 'c', 'v'}
#     match = {}
#
#     def fill_match():
#         keyboard = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
#                     ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
#                     ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
#         for i in range(3):
#             for j in range(len(keyboard[i])):
#                 alp = keyboard[i][j]
#                 match[alp] = (i, j)
#
#     def return_position(alp):
#         return match[alp]
#
#     fill_match()
#     left_position, right_position = map(return_position,input().split())
#     word = input()
#     cnt = 0
#     for alp in word:
#         nx, ny = return_position(alp)
#         if alp in left:
#             x, y = left_position
#             left_position = (nx, ny)
#         else:
#             x, y = right_position
#             right_position = (nx, ny)
#         cnt += abs(nx - x) + abs(ny - y) + 1
#     return cnt
#
# print(find_cnt())


# match
# def find_cnt():
#     def fill_match():
#         keyboard = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
#                     ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
#                     ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
#         match = {}
#         for i in range(3):
#             for j in range(len(keyboard[i])):
#                 alp = keyboard[i][j]
#                 match[alp] = (i, j)
#         return match
#
#     def return_position(alp):
#         return match[alp]
#
#     left = {'q', 'w', 'e', 'r', 't',
#             'a', 's', 'd', 'f', 'g',
#             'z', 'x', 'c', 'v'}
#     match = fill_match()
#     left_position, right_position = map(return_position,input().split())
#     word = input()
#     cnt = 0
#     for alp in word:
#         nx, ny = return_position(alp)
#         if alp in left:
#             x, y = left_position
#             left_position = (nx, ny)
#         else:
#             x, y = right_position
#             right_position = (nx, ny)
#         cnt += abs(nx - x) + abs(ny - y) + 1
#     return cnt
#
# print(find_cnt())


# right
def find_cnt():
    def fill_match():
        keyboard = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
                    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
                    ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
        match = {}
        for i in range(3):
            for j in range(len(keyboard[i])):
                alp = keyboard[i][j]
                match[alp] = (i, j)
        return match

    def return_position(alp):
        return match[alp]

    right = {'y', 'u', 'i', 'o', 'p',
            'h', 'j', 'k', 'l',
            'b', 'n', 'm'}
    match = fill_match()
    left_position, right_position = map(return_position,input().split())
    word = input()
    cnt = 0
    for alp in word:
        nx, ny = return_position(alp)
        if alp in right:
            x, y = right_position
            right_position = (nx, ny)
        else:
            x, y = left_position
            left_position = (nx, ny)
        cnt += abs(nx - x) + abs(ny - y) + 1
    return cnt

print(find_cnt())
