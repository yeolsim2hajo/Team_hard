#230124
# n = int(input())
# five = n//5
# two, min_cnt = divmod(n%5, 2)
# if min_cnt:
#     five -= 1
#     two += 3
# min_cnt = five+two if five >= 0 else -1
# print(min_cnt)

# remain
# n = int(input())
# five = n//5
# two, remain = divmod(n%5, 2)
# if remain:
#     five -= 1
#     two += 3
# min_cnt = five+two if five >= 0 else -1
# print(min_cnt)

# 함수
# def find_min_cnt(n):
#     five = n//5
#     two, remain = divmod(n%5, 2)
#     if remain:
#         five -= 1
#         two += 3
#     min_cnt = five+two if five >= 0 else -1
#     return min_cnt
#
# n = int(input())
# print(find_min_cnt(n))


# 나눠서 - 시간 더 걸림
# def find_min_cnt(n):
#     five = n//5
#     two, remain = divmod(n%5, 2)
#     if remain:
#         five -= 1
#         two += 3
#         min_cnt = five+two if five >= 0 else -1
#         return min_cnt
#     return five+two
#
# n = int(input())
# print(find_min_cnt(n))


# 먼저 종료
def find_min_cnt(n):
    five = n//5
    two, remain = divmod(n%5, 2)
    min_cnt = five+two
    if remain == 0:
        return min_cnt
    min_cnt = min_cnt+2 if five >= 1 else -1
    return min_cnt

n = int(input())
print(find_min_cnt(n))
