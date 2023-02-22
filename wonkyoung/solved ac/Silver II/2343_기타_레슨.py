#230222
# N, M = map(int, input().split())
# lectures = list(map(int, input().split()))
# total = max_length = 0
# for lecture in lectures:
#     total += lecture
#     if lecture > max_length:
#         max_length = lecture
#
# start, end = max_length, total
# while start <= end:
#     size = (start + end)//2
#     blue_ray, cnt = 0, 1
#     for lecture in lectures:
#         blue_ray += lecture
#         if blue_ray > size:
#             cnt += 1
#             blue_ray = lecture
#             if cnt > M:
#                 start = size + 1
#                 break
#     else:
#         end = size - 1
# print(start)

#
# N, M = map(int, input().split())
# lectures = list(map(int, input().split()))
# total = max_length = 0
# for lecture in lectures:
#     total += lecture
#     if lecture > max_length:
#         max_length = lecture
#
# start, end = max_length, total
# while start <= end:
#     size = (start + end)//2
#     blue_ray, cnt = 0, 1
#     for lecture in lectures:
#         blue_ray += lecture
#         if blue_ray > size:
#             cnt += 1
#             blue_ray = lecture
#     if cnt > M:
#         start = size + 1
#     else:
#         end = size - 1
# print(start)


#
# def find_size():
#     N, M = map(int, input().split())
#     lectures = list(map(int, input().split()))
#     total = max_length = 0
#     for lecture in lectures:
#         total += lecture
#         if lecture > max_length:
#             max_length = lecture
#     def binary_search():
#         start, end = max_length, total
#         while start <= end:
#             size = (start + end)//2
#             blue_ray, cnt = 0, 1
#             for lecture in lectures:
#                 blue_ray += lecture
#                 if blue_ray > size:
#                     cnt += 1
#                     blue_ray = lecture
#             if cnt > M:
#                 start = size + 1
#             else:
#                 end = size - 1
#         return start
#     return binary_search()
# print(find_size())

#
# def find_size():
#     N, M = map(int, input().split())
#     lectures = list(map(int, input().split()))
#     total = sum(lectures)
#     max_length = max(lectures)
#     def binary_search():
#         start, end = max_length, total
#         while start <= end:
#             size = (start + end)//2
#             blue_ray, cnt = 0, 1
#             for lecture in lectures:
#                 blue_ray += lecture
#                 if blue_ray > size:
#                     cnt += 1
#                     blue_ray = lecture
#             if cnt > M:
#                 start = size + 1
#             else:
#                 end = size - 1
#         return start
#     return binary_search()
# print(find_size())

#
# def find_size():
#     N, M = map(int, input().split())
#     lectures = list(map(int, input().split()))
#     total = sum(lectures)
#     max_length = max(*lectures, total//M)
#     def binary_search():
#         start, end = max_length, total
#         while start <= end:
#             size = (start + end)//2
#             blue_ray, cnt = 0, 1
#             for lecture in lectures:
#                 blue_ray += lecture
#                 if blue_ray > size:
#                     cnt += 1
#                     blue_ray = lecture
#             if cnt > M:
#                 start = size + 1
#             else:
#                 end = size - 1
#         return start
#     return binary_search()
# print(find_size())

# 이분탐색 여러 번 사용하려다 실패