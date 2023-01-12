#221205
# from collections import deque
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     people, stairs = [], []
#     for i in range(N):
#         info = list(map(int, input().split()))
#         for j in range(N):
#             if info[j] == 1:
#                 people.append((i, j))
#             elif info[j] > 1:
#                 stairs.append((i, j, info[j]))
#     for i in range(len(people)):
#         person = people[i]
#         people[i] = (abs(person[0] - stairs[0][0]) + abs(person[1] - stairs[0][1]), abs(person[0] - stairs[1][0]) + abs(person[1] - stairs[1][1]), *person)
#     people.sort(key= lambda person: (person[0], -person[1]))
#     people = deque(people)
#     total_time = cnt_one = cnt_two = one = 0
#     two = -1
#     one_stair, two_stair = [0]*3, [0]*3
#     complete = False
#     # one = people.popleft()[0]
#     while people:
#         total_time += 1
#         if cnt_one:
#             for i in range(cnt_one):
#                 one_stair[i] += 1
#                 if one_stair[i] == stairs[2]:
#                     one_stair[i] = 0
#                     cnt_one -= 1
#                     complete = True
#             if complete:
#                 one_stair = one_stair[1:] + one_stair[0:1]
#                 complete = False
#         if cnt_two:
#             for i in range(cnt_two):
#                 two_stair[i] += 1
#                 if two_stair[i] == stairs[2]:
#                     two_stair[i] = 0
#                     cnt_two -= 1
#                     complete = True
#             if complete:
#                 two_stair = two_stair[1:] + two_stair[0:1]
#                 complete = False
#
#
#         if total_time < people[one][0]:
#             if cnt_one < 3:
#                 cnt_one += 1
#                 people.popleft()
#         if total_time < people[two][1]:
#             if cnt_two < 3:
#                 cnt_two += 1
#             else:
#                 pass