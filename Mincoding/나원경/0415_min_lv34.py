#3 민코 북카페
# N = int(input())
# book_list = input().split()
# book_list.sort()
# M = int(input())
# for _ in range(M):
#     book, limit_time = input().split()
#     limit_time = int(limit_time)
#     cnt = 1
#     left = 0
#     right = N-1
#     result = 'fail'
#     while cnt <= limit_time:
#         mid = (left+right)//2
#         if book_list[mid] == book:
#             result = 'pass'
#             break
#         elif book_list[mid] > book:
#             right = mid-1
#         else:
#             left = mid + 1
#         cnt += 1
#     print(result)


# 클라우드 데이터 백업
# N = int(input())
# info = [input() for _ in range(N)]
# top = 0
# bottom = N-1
# while top <= bottom:
#     mid = (top+bottom)//2
#     if info[mid][0] == '#':
#         top = mid+1
#     else:
#         bottom = mid-1
# for j in range(N):
#     if info[bottom][j] == '0':
#         i = bottom
#         break
# else:
#     for j in range(N):
#         if info[top][j] == '0':
#             i = top
#             break
# print(i, j-1)