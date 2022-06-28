#16922 로마 숫자 만들기 - dfs X
# N = int(input())
# numbers = [1,5,10,50]
# new_numbers = numbers[:]
# def plus(a):
#     return a + numbers[i]
# turn = 1
# while turn < N:
#     comb = set()
#     for i in range(4):
#         comb.update(map(plus, new_numbers))
#     new_numbers = list(comb)
#     turn += 1
# print(len(new_numbers))


#1254 팰린드롬 만들기
# S = input()
# min_length = len(S)
# palindrome = S
# length = 0
# while True:
#     if palindrome == palindrome[::-1]:
#         min_length += length
#         break
#     palindrome = S
#     length += 1
#     palindrome += S[:length][::-1]
# print(min_length)


# S = input()
# min_length = len(S)
# palindrome = S
# length = 0
# while True:
#     if palindrome == palindrome[::-1]:
#         min_length += length
#         break
#     length += 1
#     palindrome = S + S[:length][::-1]
# print(min_length)


#3343 장미
# N, cnt1, price1, cnt2, price2 = map(int, input().split())
# if cnt1 > cnt2:
#     cnt1, cnt2, price1, price2 = cnt2, cnt1, price2, price1
# limit1 = N//cnt1 + 1 if N%cnt1 else N//cnt1
# limit2 = N//cnt2 + 1 if N%cnt2 else N//cnt2
# min_price = min(price1 * limit1, price2 * limit2)
# flower_price1 = round(price1/cnt1, -10)
# flower_price2 = round(price2/cnt2, -10)
# def conf():
#     if flower_price1 > flower_price2:
#         pass
#     elif flower_price1 < flower_price2:
#         return cnt1
#     else:
#         return cnt2
# start = 1
# end = limit1
# while end < start:
#     mid = (end+start)//2
#     quot, remain = divmod(N - cnt1 * mid, cnt2)
#     if remain:
#         quot += 1
#     min_price = min(min_price, price1 * mid + price2 * quot)
# print(min_price)