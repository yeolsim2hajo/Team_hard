#16953 A -> B
# def find_cnt():
#     A, B = map(int, input().split())
#     cnt = 1
#     while A != B:
#         if A > B:
#             return -1
#         elif B%2 == 0:
#             cnt += 1
#             B //= 2
#         elif B%10 == 1:
#             cnt += 1
#             B //= 10
#         else:
#             return -1
#     return cnt
# print(find_cnt())


# 시간 덜 걸림
# def find_cnt():
#     A, B = map(int, input().split())
#     cnt = 1
#     while A != B:
#         two = B%2
#         if A > B or (two and B%10 != 1):
#             return -1
#         cnt += 1
#         if two:
#             B //= 10
#         else:
#             B //= 2
#     return cnt
# print(find_cnt())


# 시간 더 걸림
# def find_cnt():
#     A, B = map(int, input().split())
#     cnt = 1
#     while A < B:
#         two = B%2
#         if two and B%10 != 1:
#             return -1
#         cnt += 1
#         if two:
#             B //= 10
#         else:
#             B //= 2
#     if A != B:
#         return -1
#     return cnt
# print(find_cnt())


# 시간 더더 걸림
# def find_cnt():
#     A, B = map(int, input().split())
#     cnt = 1
#     while True:
#         if A == B:
#             return cnt
#         two = B%2
#         if A > B or (two and B%10 != 1):
#             return -1
#         cnt += 1
#         if two:
#             B //= 10
#         else:
#             B //= 2
# print(find_cnt())
