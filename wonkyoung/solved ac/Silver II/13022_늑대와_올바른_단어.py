#221212
# def is_correct(word):
#     wolf = [0] * 4
#     match = {'w': 0, 'o': 1, 'l': 2, 'f': 3}
#     possible = False
#     cnt = 0
#     for alp in word:
#         cnt += 1
#         index = match[alp]
#         if index == 0:
#             if not possible:
#                 for i in range(-1, 3):
#                     if wolf[i] != wolf[i + 1]:
#                         return 0
#             possible = True
#             wolf[index] += 1
#         else:
#             wolf[index] += 1
#             value = wolf[index]
#             for i in range(index-1):
#                 if wolf[i] != wolf[i+1]:
#                     return 0
#             for i in range(index):
#                 if wolf[i] < value:
#                     return 0
#             possible = False
#     return 1
# word = input()
# print(is_correct(word))



#221217
# def is_correct_word(arg):
#     wolf = [0] * 4
#     visited = [False] * 4
#     cnt = 0
#     match = {'w': 0, 'o': 1, 'l': 2, 'f': 3}
#     for alp in arg:
#         index = match[alp]
#         if index:
#             if cnt < wolf[index]:
#                 return 0
#             if not visited[index]:
#                 for i in range(1, index):
#                     if wolf[i] != cnt:
#                         return 0
#                 visited[:index] = [False] * index
#                 visited[index] = True
#             wolf[index] += 1
#         else:
#             if not visited[index]:
#                 for i in range(1, 4):
#                     if wolf[i] != cnt:
#                         return 0
#                 visited = [False] * 4
#                 visited[index] = True
#             cnt += 1
#     for i in range(1, 4):
#         if wolf[i] != cnt:
#             return 0
#     return 1
#
# word = input()
# print(is_correct_word(word))


# 겹치는 부분 함수화 => 시간 더 걸림
# def is_correct_word(arg):
#     wolf = [0] * 4
#     visited = [False] * 4
#     cnt = 0
#     match = {'w': 0, 'o': 1, 'l': 2, 'f': 3}
#
#     def is_cnt(end):
#         for i in range(1, end):
#             if wolf[i] != cnt:
#                 return 0
#         visited[:index] = [False] * index
#         visited[index] = True
#         return 1
#
#     for alp in arg:
#         index = match[alp]
#         if index:
#             if cnt < wolf[index]:
#                 return 0
#             if not visited[index]:
#                 if not is_cnt(index):
#                     return 0
#             wolf[index] += 1
#         else:
#             if not visited[index]:
#                 if not is_cnt(4):
#                     return 0
#             cnt += 1
#     if not is_cnt(4):
#         return 0
#
#     return 1
#
# word = input()
# print(is_correct_word(word))


# cnt 없애고 index 분기 없앰
def is_correct_word(arg):
    wolf = [0] * 4
    visited = [False] * 4
    match = {'w': 0, 'o': 1, 'l': 2, 'f': 3}
    for alp in arg:
        index = match[alp]
        if not visited[index]:
            limit = index or 4
            for i in range(1, limit):
                if wolf[i] != wolf[0]:
                    return 0
            visited[:index] = [False] * index
            visited[index] = True
        wolf[index] += 1

    for i in range(1, 4):
        if wolf[i] != wolf[0]:
            return 0
    return 1

word = input()
print(is_correct_word(word))