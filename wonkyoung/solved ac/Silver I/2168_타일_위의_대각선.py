# 230305
# https://www.acmicpc.net/problem/2168
# def cnt_tile(x, y):
#     if x == y:
#         return x
#     if y > x:
#         x, y = y, x
#     if x % y == 0:
#         return x
#     gcd, number = x, y
#     while number:
#         gcd, number = number, gcd%number
#     x //= gcd
#     y //= gcd
#     return (x + y - 1) * gcd
# print(cnt_tile(*map(int, input().split())))


#
# def cnt_tile(x, y):
#     if y > x:
#         x, y = y, x
#     gcd, number = x, y
#     while number:
#         gcd, number = number, gcd%number
#     x //= gcd
#     y //= gcd
#     return (x + y - 1) * gcd
# print(cnt_tile(*map(int, input().split())))

#
# def cnt_tile(x, y):
#     if x == y:
#         return x
#     if y > x:
#         x, y = y, x
#     if x % y == 0:
#         return x
#     gcd, number = x, y
#     while number:
#         gcd, number = number, gcd%number
#     return x + y - gcd
# print(cnt_tile(*map(int, input().split())))

#
# def cnt_tile(x, y):
#     if y > x:
#         x, y = y, x
#     if x % y == 0:
#         return x
#     gcd, number = x, y
#     while number:
#         gcd, number = number, gcd%number
#     return x + y - gcd
# print(cnt_tile(*map(int, input().split())))

#
def cnt_tile(x, y):
    if y > x:
        x, y = y, x
    if x % y == 0:
        return x
    gcd, number = x, y
    while number:
        gcd, number = number, gcd%number
    x //= gcd
    y //= gcd
    return (x + y - 1) * gcd
print(cnt_tile(*map(int, input().split())))