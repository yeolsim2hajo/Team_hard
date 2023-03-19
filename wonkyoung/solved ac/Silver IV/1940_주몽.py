#230319
# N = int(input())
# M = int(input())
# material_set = set(map(int, input().split()))
# visited = set()
# cnt = 0
# for material in material_set:
#     if material not in visited:
#         visited.add(material)
#         remain = M - material
#         if remain in material_set and remain not in visited:
#             cnt += 1
#             visited.add(remain)
# print(cnt)


#
# N = int(input())
# M = int(input())
# material_set = set(map(int, input().split()))
# def find_cnt():
#     visited = set()
#     cnt = 0
#     for material in material_set:
#         if material not in visited:
#             visited.add(material)
#             remain = M - material
#             if remain in material_set and remain not in visited:
#                 cnt += 1
#                 visited.add(remain)
#     return cnt
# print(find_cnt())


#
# N = int(input())
# M = int(input())
# material_set = set(map(int, input().split()))
# def find_cnt():
#     remain_list = set(material_set)
#     cnt = 0
#     for material in material_set:
#         if material in remain_list:
#             remain_list.remove(material)
#             remain = M - material
#             if remain in remain_list:
#                 cnt += 1
#                 remain_list.remove(remain)
#     return cnt
# print(find_cnt())


#
# N = int(input())
# M = int(input())
# material_list = sorted(map(int, input().split()))
# def find_cnt():
#     start = cnt = 0
#     end = N - 1
#     while start < end:
#         total = material_list[start] + material_list[end]
#         if total > M:
#             end -= 1
#         elif total < M:
#             start += 1
#         else:
#             cnt += 1
#             end -= 1
#             start += 1
#
#     return cnt
# print(find_cnt())


#
# N = int(input())
# M = int(input())
# material_list = list(map(int, input().split()))
# def find_cnt():
#     material_list.sort()
#     start = cnt = 0
#     end = N - 1
#     while start < end:
#         total = material_list[start] + material_list[end]
#         if total > M:
#             end -= 1
#         elif total < M:
#             start += 1
#         else:
#             cnt += 1
#             end -= 1
#             start += 1
#
#     return cnt
# print(find_cnt())


#
N = int(input())
M = int(input())
material_list = sorted(map(int, input().split()))
def find_cnt():
    start = cnt = 0
    end = N - 1
    smaller, greater = material_list[start], material_list[end]
    total = smaller + greater
    while start < end:
        if total > M:
            end -= 1
            total -= greater - material_list[end]
            greater = material_list[end]
        elif total < M:
            start += 1
            total -= smaller - material_list[start]
            smaller = material_list[start]
        else:
            cnt += 1
            end -= 1
            start += 1
            smaller, greater = material_list[start], material_list[end]
            total = smaller + greater

    return cnt
print(find_cnt())