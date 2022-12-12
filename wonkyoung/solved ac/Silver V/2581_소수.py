# 220915
# M = int(input())
# N = int(input())
# total, min_val = 0, -1
# numbers = set(range(2, N+1))
# for i in range(2, N+1):
#     for j in range(2*i, N+1, i):
#         if j in numbers:
#             numbers.remove(j)
#
# for i in range(M, N+1):
#     if i in numbers:
#         total += i
#         if min_val == -1:
#             min_val = i
#
# if total:
#     print(total, min_val, sep='\n')
# else:
#     print(min_val)


# remove -> discard 시간 더 걸림
# M = int(input())
# N = int(input())
# total, min_val = 0, -1
# numbers = set(range(2, N+1))
# for i in range(2, N+1):
#     for j in range(2*i, N+1, i):
#         numbers.discard(j)
#
# for i in range(M, N+1):
#     if i in numbers:
#         total += i
#         if min_val == -1:
#             min_val = i
#
# if total:
#     print(total, min_val, sep='\n')
# else:
#     print(min_val)


# 시간 같음
# M = int(input())
# N = int(input())
# total, min_val = 0, N
# numbers = set(range(2, N+1))
# for i in range(2, N+1):
#     for j in range(2*i, N+1, i):
#         if j in numbers:
#             numbers.remove(j)
#
# for i in range(M, N+1):
#     if i in numbers:
#         total += i
#         min_val = min(min_val, i)
#
# if total:
#     print(total, min_val, sep='\n')
# else:
#     print(-1)


# 시간 76ms
# def main():
#     M = int(input())
#     N = int(input())
#     total, min_val = 0, -1
#     numbers = set(range(2, N+1))
#     for i in range(2, N+1):
#         for j in range(2*i, N+1, i):
#             if j in numbers:
#                 numbers.remove(j)
#
#     for i in range(M, N+1):
#         if i in numbers:
#             total += i
#             if min_val == -1:
#                 min_val = i
#
#     if total:
#         print(total, min_val, sep='\n')
#     else:
#         print(min_val)
# main()
