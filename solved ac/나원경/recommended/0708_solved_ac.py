#19948 음유시인 영재
# poet = input()
# space = int(input())
# keyboard = input().split()
# if poet.count(' ') > space:
#     print(-1)
# else:
#     def find_answer():
#         check = {}
#         answer = poet[0]
#         for i in range(26):
#             check[chr(i+65)] = int(keyboard[i])
#         for i in range(len(poet)):
#             alp = poet[i].upper()
#             if alp == ' ':
#                 answer += poet[i+1].upper()
#                 if check[answer[-1]] == 0:
#                     return -1
#                 check[answer[-1]] -= 1
#             elif check[alp] == 0:
#                 return -1
#             else:
#                 check[alp] -= 1
#         return answer
#     print(find_answer())


# 다른 방법
# poet = input().split()
# space = int(input())
# keyboard = input().split()
# fragment = len(poet)
# if fragment - 1 > space:
#     print(-1)
# else:
#     def find_answer():
#         check = {}
#         answer = ''
#         pre = ''
#         for i in range(26):
#             check[chr(i+65)] = int(keyboard[i])
#         for i in range(fragment):
#             for j in range(len(poet[i])):
#                 alp = poet[i][j]
#                 if alp == pre:
#                     continue
#                 alp = alp.upper()
#                 if check[alp] == 0:
#                     return -1
#                 if j == 0:
#                     answer += alp
#                 check[alp] -= 1
#                 pre = poet[i][j]
#         pre = ''
#         for alp in answer:
#             if alp == pre:
#                 continue
#             if check[alp] == 0:
#                 return -1
#             check[alp] -= 1
#             pre = alp
#         return answer
#     print(find_answer())


#19949 영재의 시험
#dfs
# answer = list(map(int, input().split()))
# length = len(answer)
# over_five = 0
# def dfs(arg=0, cnt=0, score=0, pre=0):
#     global over_five
#     if cnt >= 3:
#         return
#     if length - arg + score < 5:
#         return
#     if arg == length:
#         over_five += 1
#         return
#     for number in range(1,6):
#         new_score = score if number != answer[arg] else score+1
#         new_cnt = 1 if pre != number else cnt+1
#         dfs(arg+1, new_cnt, new_score, number)
# dfs()
# print(over_five)

#dfs - path - 시간 더 걸림
# answer = list(map(int, input().split()))
# length = len(answer)
# over_five = 0
# path = [0]
# def dfs(arg=0, cnt=0, score=0):
#     global over_five
#     if cnt >= 3:
#         return
#     if length - arg + score < 5:
#         return
#     if arg == length:
#         over_five += 1
#         return
#     for number in range(1,6):
#         new_score = score if number != answer[arg] else score+1
#         new_cnt = 1 if path[-1] != number else cnt+1
#         path.append(number)
#         dfs(arg+1, new_cnt, new_score)
#         path.pop()
# dfs()
# print(over_five)

#bfs
# answer = list(map(int, input().split()))
# length = len(answer)
# def bfs():
#     from collections import deque
#     over_five = 0
#     q = deque()
#     q.append((0,0,0,0))
#     while q:
#         idx, cnt, score, pre = q.popleft()
#         if cnt >= 3 or length - idx + score < 5:
#             continue
#         if idx == length:
#             over_five += 1
#             continue
#         for number in range(1,6):
#             new_score = score if number != answer[idx] else score+1
#             new_cnt = 1 if pre != number else cnt+1
#             q.append((idx+1, new_cnt, new_score, number))
#     return over_five
# print(bfs())


#다른 방법
# answer = list(map(int, input().split()))
# length = len(answer)
# case = 0
# def conf_answer(first):
#     solved = [first]
#     score = 0 if first != answer[0] else 1
#     def cnt_score():
#         global case
#         nonlocal score
#         for j in range(1, length):
#             if answer[j] == young_jae[j]:
#                 score += 1
#             if score >= 5:
#                 case += 1
#                 return
#
#     def make_list():
#         nonlocal young_jae
#         while True:
#             young_jae = solved[:]
#             cnt_score()
#
#     for _ in range(1, length):
#         make_list()
#
#
# for i in range(length):
#     conf_answer(i)
