#66 블럭탑 쌓기
# top_or_not = input().split()
# rule = input()
# ans = []
# for blocks in top_or_not:
#     idx = -1
#     for block in blocks[::-1]:
#         if block == rule[idx]:
#             idx -= 1
#         if -idx > len(rule):
#             ans.append('가능')
#             break
#     else:
#         for block in blocks[::-1]:
#             if block == rule[idx]:
#                 ans.append('불가능')
#                 break
#         else:
#             ans.append('가능')
# print(ans)


#67 민규의 악수
# n = int(input())
# people = int((2 * n) ** (0.5)) # 민규 제외 사람 추정
# while True:
#     if (people ** 2 + people) // 2 > n:
#         total = (people ** 2 - people) // 2
#         break
#     people += 1
# print([n-total,people+1])


#68 버스 시간표
# bus = input().split()
# now = list(map(int, input().split(':')))
# answer = []
# for time in bus:
#     time_sp = list(map(int,time.split(':')))
#     total_minute = (time_sp[0]-now[0]) * 60 + time_sp[1]-now[1]
#     if total_minute < 0:
#         answer.append('지나갔습니다')
#     else:
#         hour, minute = divmod(total_minute,60)
#         print(hour, minute)
#         if hour >= 10 and minute >= 10:
#             answer.append('{}시간 {}분'.format(hour, minute))
#         elif hour >= 10:
#             answer.append('{}시간 0{}분'.format(hour, minute))
#         elif minute >= 10:
#             answer.append('0{}시간 {}분'.format(hour, minute))
#         else:
#             answer.append('0{}시간 0{}분'.format(hour, minute))
# print(answer)

