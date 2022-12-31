#221231
# import sys
# new_input = sys.stdin.readline
# N, K = map(int, new_input().split())
# level_list = sorted([int(new_input()) for _ in range(N)])
# min_level = level_list[0]
# for i in range(N-1):
#     dif = level_list[i+1] - level_list[i]
#     if K >= dif * (i+1):
#         K -= dif * (i+1)
#         min_level += dif
#     else:
#         min_level += K // (i+1)
#         break
# else:
#     min_level += K // N
#
# print(min_level)



# 함수형
def find_dif():
    import sys
    new_input = sys.stdin.readline
    N, K = map(int, new_input().split())
    level_list = sorted([int(new_input()) for _ in range(N)])
    min_level = level_list[0]
    for i in range(N-1):
        dif = level_list[i+1] - level_list[i]
        minus = dif * (i+1)
        if K >= minus:
            K -= minus
            min_level += dif
        else:
            return min_level + K // (i+1)
    return min_level + K // N

print(find_dif())

