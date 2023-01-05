#230105
# import sys
# new_input = sys.stdin.readline
# N, K = map(int, new_input().split())
# min_val, max_val = 1e6, 0
# bucket_info = []
#
# for _ in range(N):
#     bucket_info.append(list(map(int,new_input().split())))
#     index = bucket_info[-1][1]
#     if index > max_val:
#         max_val = index
#     if index < min_val:
#         min_val = index
#
# position = [0] * (max_val+1)
# for bucket, index in bucket_info:
#     position[index] = bucket
# max_total = total = sum(position[min_val:min_val+2*K+1])
# for i in range(min_val, max_val-2*K):
#     total += (position[i+2*K+1] - position[i])
#     max_total = max(max_total, total)
# print(max_total)


# 함수화
# def fill_bucket():
#     import sys
#     new_input = sys.stdin.readline
#     N, K = map(int, new_input().split())
#     min_val, max_val = 1e6, 0
#     bucket_info = []
#     for _ in range(N):
#         bucket_info.append(list(map(int,new_input().split())))
#         index = bucket_info[-1][1]
#         if index > max_val:
#             max_val = index
#         if index < min_val:
#             min_val = index
#
#     position = [0] * (max_val+1)
#     def fill_position():
#         for bucket, index in bucket_info:
#             position[index] = bucket
#     def find_max():
#         max_total = total = sum(position[min_val:min_val+2*K+1])
#         for i in range(min_val, max_val-2*K):
#             total += (position[i+2*K+1] - position[i])
#             max_total = max(max_total, total)
#         return max_total
#     fill_position()
#     return find_max()
# print(fill_bucket())


# 고정
# def fill_bucket():
#     import sys
#     new_input = sys.stdin.readline
#     N, K = map(int, new_input().split())
#     min_val, max_val = 1e6, 0
#     position = [0] * int(1e6)
#     for _ in range(N):
#         bucket, index = map(int,new_input().split())
#         if index > max_val:
#             max_val = index
#         if index < min_val:
#             min_val = index
#         position[index] = bucket
#
#     def find_max():
#         max_total = total = sum(position[min_val:min_val+2*K+1])
#         for i in range(min_val, max_val-2*K):
#             total += (position[i+2*K+1] - position[i])
#             max_total = max(max_total, total)
#         return max_total
#
#     return find_max()
# print(fill_bucket())


# 최적화 시도
def fill_bucket():
    import sys
    new_input = sys.stdin.readline
    N, K = map(int, new_input().split())
    min_val, max_val = 1e6, 0
    position = [0] * (int(1e6) + 1)
    for _ in range(N):
        bucket, index = map(int,new_input().split())
        max_val = max(max_val, index)
        min_val = min(min_val, index)
        position[index] = bucket

    def find_max():
        max_total = total = sum(position[min_val:min_val+2*K+1])
        after, end = min_val+2*K, max_val-2*K

        for i in range(min_val, end):
            after += 1
            total += (position[after] - position[i])
            max_total = max(max_total, total)
        return max_total

    return find_max()
print(fill_bucket())


# 최적화 시도2
def fill_bucket():
    import sys
    new_input = sys.stdin.readline
    N, K = map(int, new_input().split())
    min_val, max_val = 1e6, 0
    position = [0] * (int(1e6) + 1)
    for _ in range(N):
        bucket, index = map(int,new_input().split())
        if index > max_val:
            max_val = index
        if index < min_val:
            min_val = index
        position[index] = bucket

    def find_max():
        after = min_val+2*K
        max_total = total = sum(position[min_val:after+1])
        for i in range(min_val, max_val-2*K):
            after += 1
            total += (position[after] - position[i])
            if total > max_total:
                max_total = total
        return max_total

    return find_max()
print(fill_bucket())