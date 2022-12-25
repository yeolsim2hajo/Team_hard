#221225
# start, end = map(int, input().split())
# total, n, cnt = 0, 1, 0
#
# for i in range(1, end+1):
#     cnt += 1
#     if i >= start:
#         total += n
#     if n == cnt:
#         cnt = 0
#         n += 1
# print(total)


# 함수
def solution():
    start, end = map(int, input().split())
    total = cnt = 0
    n = 1
    for i in range(1, end+1):
        cnt += 1
        if i >= start:
            total += n
        if n == cnt:
            cnt = 0
            n += 1
    return total
print(solution())