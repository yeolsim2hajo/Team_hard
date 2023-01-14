#230114
# N, K = map(int, input().split())
# temperatures = list(map(int, input().split()))
# total = max_total = sum(temperatures[:K])
# for i in range(K, N):
#     total += (temperatures[i] - temperatures[i-K])
#     if total > max_total:
#         max_total = total
# print(max_total)


#
# import sys
# new_input = sys.stdin.readline
# N, K = map(int, new_input().split())
# temperatures = list(map(int, new_input().split()))
# total = max_total = sum(temperatures[:K])
# for i in range(K, N):
#     total += (temperatures[i] - temperatures[i-K])
#     if total > max_total:
#         max_total = total
# print(max_total)


def find_max():
    N, K = map(int, input().split())
    temperatures = list(map(int, input().split()))
    total = max_total = sum(temperatures[:K])
    for i in range(K, N):
        total += (temperatures[i] - temperatures[i-K])
        if total > max_total:
            max_total = total
    return max_total
print(find_max())