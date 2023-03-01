#230301
# A, B = input().split()
# len_a, len_b = len(A), len(B)
# min_dif = len_a
# for i in range(len_b - len_a + 1):
#     dif = 0
#     for j in range(len_a):
#         if A[j] != B[i+j]:
#             dif += 1
#     if dif < min_dif:
#         min_dif = dif
# print(min_dif)

#
# def find_dif():
#     len_a, len_b = len(A), len(B)
#     min_dif = len_a
#     for i in range(len_b - len_a + 1):
#         dif = 0
#         for j in range(len_a):
#             if A[j] != B[i+j]:
#                 dif += 1
#         if dif < min_dif:
#             min_dif = dif
#     return min_dif
#
# A, B = input().split()
# print(find_dif())

#
# def find_dif():
#     len_a, len_b = len(A), len(B)
#     min_dif = len_a
#     for i in range(len_b - len_a + 1):
#         dif = 0
#         for j in range(len_a):
#             if A[j] != B[i+j]:
#                 dif += 1
#                 if dif >= min_dif:
#                     break
#         else:
#             min_dif = dif
#     return min_dif
#
# A, B = input().split()
# print(find_dif())