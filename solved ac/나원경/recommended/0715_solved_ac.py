#2346 풍선 터뜨리기
# N = int(input())
# numbers = list(map(int, input().split()))
# move = 0
# order = [0]*N
# order[0], burst = 1, numbers[0]
# def change_burst():
#     global burst
#     if burst >= N:
#         burst -= N
#     elif burst < 0:
#         burst += N
#
# for i in range(N):
#     move = 1 if numbers[burst] > 0 else -1
#     while numbers[burst] == 0:
#         burst += move
#         change_burst()
#     order[i] = burst+1
#     temp, numbers[burst] = numbers[burst], 0
#     burst += temp
#     change_burst()
# print(*order)


#2512 예산
# N = int(input())
# request = list(map(int, input().split()))
# total_budget = int(input())
# request.sort()
# budget = request[-1]
# if sum(request) > total_budget:
#     start = request[0]
#     end = budget
#     while end >= start:
#         mid = (end+start) // 2
#         total = 0
#         for i in request:
#             total += i if i < mid else mid
#         if total == total_budget:
#             budget = mid
#             break
#         elif total < total_budget:
#             start = mid + 1
#         else:
#             end = mid - 1
#     else:
#         budget = end
# print(budget)


#1037 약수
# N = int(input())
# real = sorted(list(map(int, input().split())))
# number = real[-1] * 2
# while True:
#     for i in range(N-1):
#         if number%real[i] and number!=real[i]:
#             break
#     else:
#         break
#     number += real[-1]
# print(number)


#2440 별 찍기 - 3
N = int(input())
for i in range(N):
    print('*'*(N-i))