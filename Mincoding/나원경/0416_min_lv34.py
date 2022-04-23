#5 root 계산기
# def bs(number):
#     if number == 0:
#         print(n)
#         return
#     elif number < 0:
#         return
#     else:
#         left = 0
#         right = number
#         while left < right:
#             mid = (left + right)//2
#             conf = mid**2
#             if conf == number:
#                 print(mid)
#                 return
#             elif conf < number:
#                 left = mid+1
#             else:
#                 right = mid-1
#         if left**2 < number:
#             print(left)
#         else:
#             print(right)
#
# n = int(input())
# bs(n)

#6 금 나와라 황금보자기
# def take_gold():
#     cnt = 0
#     while 1:
#         for _ in range(2):
#             rock = heapq.heappop(gold)
#             if rock[1]:
#                 if gold[0] == (rock[0],0):
#                     heapq.heappop(gold)
#                     heapq.heappush(gold,rock)
#                     cnt += 1
#                 else:
#                     print(cnt)
#                     return
#             else:
#                 cnt += 1
#
#         heapq.heappush(gold,(rock[0]*2,1))
#
# import heapq
# n = int(input())
# gold = input().split()
# for i in range(n):
#     gold[i] = (int(gold[i]),0)
# heapq.heapify(gold)
# take_gold()


