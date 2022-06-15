# 국회의원 선거 - 틀림
# import heapq
# N = int(input())
# candidate = []
# for i in range(1,N+1):
#     heapq.heappush(candidate, [-int(input()), -i])
# for i in range(N):
#     if candidate[i][1] == -1:
#         start = i
#         break
# cnt = 0
# while start:
#     parent = (start-1)//2
#     if start%2 and candidate[start][0] >= candidate[start-1][0]:
#         cnt += 1
#         candidate[start][0] -= 1
#         candidate[parent][0] += 1
#         continue
#     elif start < N-1 and start%2 == 0 and candidate[start][0] >= candidate[start+1][0]:
#         cnt += 1
#         candidate[start][0] -= 1
#         candidate[parent][0] += 1
#         continue
#     if candidate[start][0] >= candidate[parent][0]:
#         cnt += 1
#         candidate[start][0] -= 1
#         candidate[parent][0] += 1
#         continue
#     candidate[start], candidate[parent] = candidate[parent], candidate[start]
#     start = parent
# print(cnt)



    # if candidate[start][0] < candidate[parent][0]:
    #     candidate[start], candidate[parent] = candidate[parent], candidate[start]
    #     start = parent

#크리스마스 선물
# import sys, heapq
# N = int(input())
# new_input = sys.stdin.readline
# gift_list = []
# length = 0
# for _ in range(N):
#     number = new_input().rstrip()
#     if number == '0':
#         answer = -heapq.heappop(gift_list) if length else -1
#         length = length - 1 if length else 0
#         print(answer)
#     else:
#         number = list(map(int,number.split()))
#         for i in range(1,number[0]+1):
#             heapq.heappush(gift_list,-number[i])
#         length += number[0]

#2075 N번째 큰 수
# import sys,heapq
# N = int(input())
# new_input = sys.stdin.readline
# table = []
# for i in range(N):
#     row = list(map(int,new_input().split()))
#     table.extend(row)
#     heapq.heapify(table)
#     if len(table) > N:
#         for _ in range(N):
#             heapq.heappop(table)
# print(table[0])


#5619 세 번째 - 틀림
# import sys, heapq
# N = int(input())
# new_input = sys.stdin.readline
# numbers = []
# small = []
# for _ in range(N):
#     numbers.append(int(new_input().rstrip()))
#     if len(numbers) > 3:
#         numbers = heapq.nsmallest(3,numbers)
# answer = ''
# for _ in range(2):
#     answer = str(heapq.heappop(numbers)) + answer
# print(answer)


