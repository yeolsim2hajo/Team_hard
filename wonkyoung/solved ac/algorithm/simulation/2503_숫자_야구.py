#221105
# 모든 경우
# N = int(input())
# cases = set()
# cnt = 0
# complete = False
# for i in range(123, 988):
#     number = str(i)
#     if '0' not in number:
#         if len(set(map(str, number))) == 3:
#             cases.add(number)
# for _ in range(N):
#     number, strikes, balls = input().split()
#     strikes, balls = int(strikes), int(balls)
#     temp = set()
#     for case in cases:
#         copied_strikes, copied_balls = strikes, balls
#         for i in range(3):
#             if number[i] == case[i]:
#                 copied_strikes -= 1
#             elif number[i] in case:
#                 copied_balls -= 1
#         if copied_strikes == copied_balls == 0:
#             temp.add(case)
#     cases = set(temp)
# print(len(cases))


# remove 이용
# N = int(input())
# cases = set()
# cnt = 0
# complete = False
# for i in range(123, 988):
#     number = str(i)
#     if '0' not in number:
#         if len(set(map(str, number))) == 3:
#             cases.add(number)
# for _ in range(N):
#     number, strikes, balls = input().split()
#     strikes, balls = int(strikes), int(balls)
#     temp = set(cases)
#     for case in cases:
#         copied_strikes, copied_balls = strikes, balls
#         for i in range(3):
#             if number[i] == case[i]:
#                 copied_strikes -= 1
#             elif number[i] in case:
#                 copied_balls -= 1
#         if not (copied_strikes == copied_balls == 0):
#             temp.remove(case)
#     cases = set(temp)
# print(len(cases))


# heap 이용 (더 걸림)
# from heapq import heappush, heappop
# N = int(input())
# cases = set()
# for i in range(123, 988):
#     number = str(i)
#     if '0' not in number:
#         if len(set(map(str, number))) == 3:
#             cases.add(number)
# questions = []
#
# for _ in range(N):
#     number, strike, ball = input().split()
#     heappush(questions, (int(ball), -int(strike), number))
#
# for i in range(N):
#     ball, strike, number = heappop(questions)
#     temp = set(cases)
#     for case in cases:
#         copied_strikes, copied_balls = strike, ball
#         for i in range(3):
#             if number[i] == case[i]:
#                 copied_strikes += 1
#             elif number[i] in case:
#                 copied_balls -= 1
#         if not (copied_strikes == copied_balls == 0):
#             temp.remove(case)
#     cases = set(temp)
#
# print(len(cases))
