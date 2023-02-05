#230205
# 모든 경우
def only_full_bed():
    A, B, C, N = map(int, input().split())
    quot, remain = divmod(N, C)
    for _ in range(quot, -1, -1):
        new_quot, new_remain = divmod(remain, B)
        for _ in range(new_quot, -1, -1):
            if new_remain%A == 0:
                return 1
            new_remain += B
        remain += C
    return 0
print(only_full_bed())

# 나눠 떨어질 때 return
def only_full_bed():
    A, B, C, N = map(int, input().split())
    quot, remain = divmod(N, C)
    if remain == 0:
        return 1
    for _ in range(quot, -1, -1):
        new_quot, new_remain = divmod(remain, B)
        for _ in range(new_quot, -1, -1):
            if new_remain%A == 0:
                return 1
            new_remain += B
        remain += C
    return 0
print(only_full_bed())

# 추려내기 필요