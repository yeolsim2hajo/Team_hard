#221209
#221210
# 시간 초과
# import sys
# R, S = map(int, input().split())
# new_input = sys.stdin.readline
# star_position = [[] for _ in range(S)]
# ground_position = [[] for _ in range(S)]
# star_position_set, ground_position_set = set(), set()
# for i in range(R):
#     star = list(map(str, new_input().rstrip()))
#     if 'X' in star:
#         for j in range(S):
#             if star[j] == 'X':
#                 star_position[j].append(i)
#                 star_position_set.add((i, j))
#     if '#' in star:
#         for j in range(S):
#             if star[j] == '#':
#                 ground_position[j].append(i)
#                 ground_position_set.add((i, j))
#
# min_distance = R
# for j in range(S):
#     star_list, ground_list = star_position[j], ground_position[j]
#     if star_list and ground_list:
#         bottom_star = star_list[-1]
#         top_ground = ground_list[0]
#         min_distance = min(top_ground - bottom_star - 1, min_distance)
# length = len(star_position_set)
# star_position_temp = set()
# for _ in range(length):
#     i, j = star_position_set.pop()
#     star_position_temp.add((i+min_distance, j))
#
# for i in range(R):
#     row = ''
#     for j in range(S):
#         if (i, j) in star_position_temp:
#             row += 'X'
#         elif (i, j) in ground_position_set:
#             row += '#'
#         else:
#             row += '.'
#     print(row)



# 시간, 메모리 엄청
# import sys
# new_input = sys.stdin.readline
# R, S = map(int, new_input().split())
# star_position = [[] for _ in range(S)]
# ground_position = [[] for _ in range(S)]
# stars = []
# star_limit = R-1
# for i in range(R):
#     star = list(map(str, new_input().rstrip()))
#     stars.append(star)
#     for j in range(S):
#         if star[j] == 'X':
#             star_limit = i
#             star_position[j].append(i)
#         elif star[j] == '#':
#             ground_position[j].append(i)
#
# min_distance = R
# for j in range(S):
#     star_list, ground_list = star_position[j], ground_position[j]
#     if star_list and ground_list:
#         bottom_star = star_list[-1]
#         top_ground = ground_list[0]
#         min_distance = min(top_ground - bottom_star - 1, min_distance)
# for j in range(S):
#     star_list = star_position[j]
#     length = len(star_list)
#     for i in range(length-1, -1, -1):
#         index = star_list[i]
#         stars[index][j], stars[index + min_distance][j] = stars[index + min_distance][j], stars[index][j]
# for i in range(R):
#     print(*stars[i], sep='')




# 함수로
# print
# def find_result():
#     import sys
#     new_input = sys.stdin.readline
#     R, S = map(int, new_input().split())
#     star_position = [[] for _ in range(S)]
#     ground_position = [[] for _ in range(S)]
#     stars = []
#
#     def fill_list():
#         for i in range(R):
#             star = list(map(str, new_input().rstrip()))
#             stars.append(star)
#             for j in range(S):
#                 if star[j] == 'X':
#                     star_position[j].append(i)
#                 elif star[j] == '#':
#                     ground_position[j].append(i)
#
#     def find_min_distance():
#         min_distance = R
#         for j in range(S):
#             star_list, ground_list = star_position[j], ground_position[j]
#             if star_list and ground_list:
#                 bottom_star = star_list[-1]
#                 top_ground = ground_list[0]
#                 min_distance = min(top_ground - bottom_star - 1, min_distance)
#         return min_distance
#
#     def change_stars():
#         for j in range(S):
#             star_list = star_position[j]
#             length = len(star_list)
#             for i in range(length-1, -1, -1):
#                 index = star_list[i]
#                 stars[index][j], stars[index + min_distance][j] = stars[index + min_distance][j], stars[index][j]
#
#     fill_list()
#     min_distance = find_min_distance()
#     change_stars()
#
#     for i in range(R):
#         print(*stars[i], sep='')
# find_result()

# join - 시간 훨씬 덜 걸림
# def find_result():
#     import sys
#     new_input = sys.stdin.readline
#     R, S = map(int, new_input().split())
#     star_position = [[] for _ in range(S)]
#     ground_position = [[] for _ in range(S)]
#     stars = []
#
#     def fill_list():
#         for i in range(R):
#             star = list(map(str, new_input().rstrip()))
#             stars.append(star)
#             for j in range(S):
#                 if star[j] == 'X':
#                     star_position[j].append(i)
#                 elif star[j] == '#':
#                     ground_position[j].append(i)
#
#     def find_min_distance():
#         min_distance = R
#         for j in range(S):
#             star_list, ground_list = star_position[j], ground_position[j]
#             if star_list and ground_list:
#                 bottom_star = star_list[-1]
#                 top_ground = ground_list[0]
#                 min_distance = min(top_ground - bottom_star - 1, min_distance)
#         return min_distance
#
#     def change_stars():
#         for j in range(S):
#             star_list = star_position[j]
#             length = len(star_list)
#             for i in range(length-1, -1, -1):
#                 index = star_list[i]
#                 stars[index][j], stars[index + min_distance][j] = stars[index + min_distance][j], stars[index][j]
#
#     fill_list()
#     min_distance = find_min_distance()
#     change_stars()
#
#     for i in range(R):
#         print(''.join(stars[i]))
# find_result()
