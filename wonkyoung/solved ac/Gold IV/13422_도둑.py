#230309
# T = int(input())
# for _ in range(T):
#     N, M, K = map(int, input().split())
#     money = list(map(int, input().split()))
#     total = sum(money[:M])
#     cnt = 0
#     if N > M:
#         money += money[:M]
#         for i in range(N):
#             if total < K:
#                 cnt += 1
#             total += money[i+M] - money[i]
#     elif total < K:
#         cnt = 1
#     print(cnt)


#
# def find_cnt():
#     N, M, K = map(int, input().split())
#     money = list(map(int, input().split()))
#     total = sum(money[:M])
#     if N == M:
#         return 0 if total >= K else 1
#     cnt = 0
#     money += money[:M]
#     for i in range(N):
#         if total < K:
#             cnt += 1
#         total += money[i + M] - money[i]
#     return cnt
#
# T = int(input())
# for _ in range(T):
#     print(find_cnt())

#
def find_cnt(N, M, K):
    global total, money
    if N == M:
        return 0 if total >= K else 1
    cnt = 0
    money += money[:M]
    for i in range(N):
        if total < K:
            cnt += 1
        total += money[i + M] - money[i]
    return cnt

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    money = list(map(int, input().split()))
    total = sum(money[:M])
    print(find_cnt(N, M, K))