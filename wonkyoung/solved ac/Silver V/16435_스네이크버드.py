#230223
# N, L = map(int, input().split())
# fruits = sorted(map(int, input().split()))
# for fruit in fruits:
#     if fruit <= L:
#         L += 1
#     else:
#         break
# print(L)

#
# def feed():
#     N, L = map(int, input().split())
#     fruits = sorted(map(int, input().split()))
#     for fruit in fruits:
#         if fruit <= L:
#             L += 1
#         else:
#             return L
#     return L
# print(feed())

#
# def feed():
#     from heapq import heapify, heappop
#     N, L = map(int, input().split())
#     fruits = list(map(int, input().split()))
#     heapify(fruits)
#     for _ in range(N):
#         fruit = heappop(fruits)
#         if fruit <= L:
#             L += 1
#         else:
#             return L
#     return L
# print(feed())

#
def feed():
    N, L = map(int, input().split())
    fruits = sorted(map(int, input().split()))
    def find_index():
        start, end = 0, N-1
        while start <= end:
            mid = (start + end) // 2
            fruit = fruits[mid]
            if fruit < L:
                start = mid + 1
            elif fruit > L:
                end = mid - 1
            else:
                return mid
        return end

    start_i = find_index() + 1
    L += start_i

    for i in range(start_i, N):
        if fruits[i] <= L:
            L += 1
        else:
            return L
    return L
print(feed())