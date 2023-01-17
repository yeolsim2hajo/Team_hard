#230117
# N, K = map(int, input().split())
# min_balls = K*(K+1)//2
# if N >= min_balls:
#     buckets = list(range(1, K+1))
#     left_balls = (N - min_balls) % K
#     min_dif = K-1
#     if left_balls:
#         min_dif += 1
# else:
#     min_dif = -1
# print(min_dif)


#
N, K = map(int, input().split())
min_balls = K*(K+1)//2
if N >= min_balls:
    left_balls = (N - min_balls) % K
    min_dif = K-1
    if left_balls:
        min_dif += 1
else:
    min_dif = -1
print(min_dif)

# if else
# N, K = map(int, input().split())
# min_balls = K*(K+1)//2
# if N >= min_balls:
#     left_balls = (N - min_balls) % K
#     if left_balls:
#         min_dif = K
#     else:
#         min_dif = K - 1
# else:
#     min_dif = -1
# print(min_dif)

# 함수
# def find_min_dif():
#     N, K = map(int, input().split())
#     min_balls = K * (K + 1) // 2
#     if N >= min_balls:
#         left_balls = (N - min_balls) % K
#         if left_balls:
#             return K
#         return K - 1
#     else:
#         return -1
# print(find_min_dif())


# 줄임
def find_min_dif():
    N, K = map(int, input().split())
    min_balls = K * (K + 1) // 2
    if N >= min_balls:
        return K if (N - min_balls) % K else K - 1
    return -1
print(find_min_dif())


#
def find_min_dif():
    N, K = map(int, input().split())
    N -= K * (K + 1) // 2
    if N >= 0:
        if N % K:
            return K
        return K - 1
    return -1
print(find_min_dif())