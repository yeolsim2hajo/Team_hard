#221015
# 시간 초과
# from heapq import heappop, heappush
# now, dist = map(int, input().split())
# heap = []
# heappush(heap, (0, now))
#
# while True:
#     second, position = heappop(heap)
#     if position == dist:
#         break
#     elif position < dist:
#         heappush(heap, (second, position*2))
#         heappush(heap, (second+1, position+1))
#     heappush(heap, (second+1, position-1))
#
# print(second)

#221016
# from heapq import heappop, heappush
# now, dist = map(int, input().split())
# heap = []
# heappush(heap, (0, now))
# max_num = 1e5
# length = max(now, dist) * 2 + 1
# result = [max_num] * length
# result[now] = 0
# # 도착지가 출발지보다 작은 경우
# answer = now - dist
#
# # 도착지가 출발지보다 큰 경우
# if now < dist:
#     while heap:
#         second, position = heappop(heap)
#         if second > result[position]:
#             continue
#         minus, plus, multiple = position-1, position+1, position*2
#         new_sec = second + 1
#         if minus >= 0:
#             if result[minus] > new_sec:
#                 result[minus] = new_sec
#                 heappush(heap, (new_sec, minus))
#         if plus < length:
#             if result[plus] > new_sec:
#                 result[plus] = new_sec
#                 heappush(heap, (new_sec, plus))
#         if multiple < length:
#             if result[multiple] > second:
#                 result[multiple] = second
#                 heappush(heap, (second, multiple))
#     answer = result[dist]
# print(answer)


# if 제거 - 틀림
from heapq import heappop, heappush
now, dist = map(int, input().split())
heap = []
heappush(heap, (0, now))
max_num = 1e5
length = max(now, dist) * 2 + 1
result = [max_num] * length
result[now] = 0
while heap:
    second, position = heappop(heap)
    if second > result[position]:
        continue
    minus, plus, multiple = position-1, position+1, position*2
    new_sec = second + 1
    if minus >= 0:
        if result[minus] > new_sec:
            result[minus] = new_sec
            heappush(heap, (new_sec, minus))
    if plus < length:
        if result[plus] > new_sec:
            result[plus] = new_sec
            heappush(heap, (new_sec, plus))
    if multiple < length:
        if result[multiple] > second:
            result[multiple] = second
            heappush(heap, (second, multiple))
print(result[dist])
