#230212
# def cnt_recycle():
#     N = int(input())
#     store = input()
#     limit, cnt = len(store), 0
#     first, second = store[:2]
#
#     def possible_signboard():
#         nonlocal cnt
#         for i in position_dict[first]:
#             for j in position_dict[second]:
#                 if i < j:
#                     dif = j - i
#                     new_i = j + dif
#                     for k in range(2, limit):
#                         if new_i >= length or store[k] != signboard[new_i]:
#                             break
#                         new_i += dif
#                     else:
#                         cnt += 1
#                         return
#
#     for _ in range(N):
#         signboard = input()
#         length = len(signboard)
#         position_dict = {alp: [] for alp in store}
#         for i in range(length):
#             alp = signboard[i]
#             if position_dict.get(alp, -1) != -1:
#                 position_dict[alp].append(i)
#         possible_signboard()
#     return cnt
# print(cnt_recycle())


#
# def cnt_recycle():
#     def possible_signboard():
#         nonlocal cnt
#         for i in position_dict[first]:
#             for j in position_dict[second]:
#                 if i < j:
#                     dif = j - i
#                     new_i = j + dif
#                     for k in range(2, limit):
#                         if new_i >= length or store[k] != signboard[new_i]:
#                             break
#                         new_i += dif
#                     else:
#                         cnt += 1
#                         return
#     def fill_dict():
#         for i in range(length):
#             alp = signboard[i]
#             if position_dict.get(alp, -1) != -1:
#                 position_dict[alp].append(i)
#
#     limit, cnt = len(store), 0
#     first, second = store[:2]
#     for _ in range(N):
#         signboard = input()
#         length = len(signboard)
#         position_dict = {alp: [] for alp in store}
#         fill_dict()
#         possible_signboard()
#     return cnt
#
# N = int(input())
# store = input()
# print(cnt_recycle())


#
def cnt_recycle(N, store):
    def possible_signboard(first_dict, second_dict):
        nonlocal cnt
        for i in first_dict:
            for j in second_dict:
                if i < j:
                    dif = j - i
                    new_i = j + dif
                    for k in range(2, limit):
                        if new_i >= length or store[k] != signboard[new_i]:
                            break
                        new_i += dif
                    else:
                        cnt += 1
                        return
    def fill_dict():
        for i in range(length):
            alp = signboard[i]
            if position_dict.get(alp, -1) != -1:
                position_dict[alp].append(i)

    limit, cnt = len(store), 0
    first, second = store[:2]
    for _ in range(N):
        signboard = input()
        length = len(signboard)
        position_dict = {alp: [] for alp in store}
        fill_dict()
        possible_signboard(position_dict[first], position_dict[second])
    return cnt

N = int(input())
store = input()
print(cnt_recycle(N, store))







