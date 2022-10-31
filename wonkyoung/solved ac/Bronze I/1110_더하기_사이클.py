#221031
# N = int(input())
# cnt, number = 1, N
# while True:
#     total = sum(divmod(number, 10))
#     number = number%10 * 10 + total%10
#     if N == number:
#         break
#     cnt += 1
# print(cnt)


def main():
    N = int(input())
    cnt, number = 1, N
    while True:
        total = sum(divmod(number, 10))
        number = number%10 * 10 + total%10
        if N == number:
            return cnt
        cnt += 1
print(main())