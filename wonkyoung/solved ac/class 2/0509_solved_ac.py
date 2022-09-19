#2108 통계학

# 시간 초과
# N = int(input())
# numbers = []
# check = {}
# for i in range(N):
#     numbers.append(int(input()))
#     if check.get(numbers[i],-1) == -1:
#         check[numbers[i]] = 1
#     else:
#         check[numbers[i]] += 1
#     for j in range(i-1,-1,-1):
#         if numbers[j] > numbers[j+1]:
#             numbers[j+1], numbers[j] = numbers[j], numbers[j+1]
#
# total = 0
# max_num = -4000
# min_num = 4000
# max_cnt = 0
# most_freq = set()
# for number in numbers:
#     total += number
#     if number < min_num:
#         min_num = number
#     if number > max_num:
#         max_num = number
#     if check[number] > max_cnt:
#         max_cnt = check[number]
#         most_freq = {number}
#     elif check[number] == max_cnt:
#         most_freq.add(number)
# if len(most_freq) >= 2:
#     most_freq = sorted(list(most_freq))[1]
# else:
#     most_freq = most_freq.pop()
#
# print(f'{round(total/N)}\n{numbers[N//2]}\n{most_freq}\n{max_num-min_num}')

# 시간초과
# N = int(input())
# numbers = [int(input()) for _ in range(N)]
# max_cnt = 0
# check = set(numbers)
# numbers.sort()
# candidates = []
# for element in check:
#     cnt = numbers.count(element)
#     if cnt > max_cnt:
#         max_cnt = cnt
#         candidates = [element]
#     elif cnt == max_cnt:
#         candidates.append(element)
# if len(candidates) >= 2:
#     candidates.sort()
#     candidates = [candidates[1]]
#
# print(f'{round(sum(numbers)/N)}\n{numbers[N//2]}\n{candidates[0]}\n{max(numbers)-min(numbers)}')


#2164 카드2
# N = int(input())
# if N == 1:
#     print(1)
# elif N % 2 == 0:
#     number = 0
#     while N > 1:
#         N //= 2
#         number += 1
#     print(2**number)
# else:
#     numbers = set(range(1,N//2+1))
#     number = 1
#     while True:
#         try:
#             numbers.remove(number)
#             number +=


#2231 분해합
# N = int(input())
# str_N = str(N)
# length = len(str_N)
# total = sum([int(n) for n in str_N])
# min_val
#
# for i in range(10**(length-1),N - total+1):
#
# else:
#     print(0)


#2292 벌집
# N = int(input())
# cnt = 1
# if N > 1:
#     while True:
#         if N <= 6*(cnt**2+cnt)//2 + 1:
#             cnt += 1
#             break
#         cnt += 1
# print(cnt)
