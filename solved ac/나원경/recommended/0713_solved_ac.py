#1503 세 수 고르기
# N, M = map(int, input().split())
# S = set(map(int, input().split()))
# if M != 1000:
#     min_val = 1e9
#     def find_dif():
#         global min_val
#         for x in range(1,1001):
#             if x not in S and min_val > N-x:
#                 for y in range(1,1001):
#                     sub = x*y
#                     if y not in S and min_val > N-sub:
#                         z = N // sub
#                         if z in S or z == 0:
#                             for i in range(1,1001):
#                                 if z+i > 1000 or z-i < 0:
#                                     break
#                                 if z+i not in S:
#                                     min_val = min(min_val, abs(N-sub*(z+i)))
#                                 if z-i not in S:
#                                     min_val = min(min_val, abs(N-sub*(z-i)))
#                         else:
#                             min_val = min(min_val, abs(N-sub*z))
#                             if z < 1000 and z + 1 not in S:
#                                 min_val = min(min_val, abs(N - sub * (z + 1)))
#                             if z > 1 and z - 1 not in S:
#                                 min_val = min(min_val, abs(N - sub * (z - 1)))
#     find_dif()
# else:
#     min_val = N
# print(min_val)

# dfs 틀림
# N, M = map(int, input().split())
# S = set(map(int,input().split()))
# if M == 0:
#     min_dif = 0
# else:
#     min_dif = 1e9
#     def find_dif(arg=0, multiple=1):
#         global min_dif
#         if abs(N - multiple) >= min_dif:
#             return
#         if arg == 3:
#             min_dif = abs(N - multiple)
#             return
#         for i in range(1,1001):
#             if i not in S:
#                 find_dif(arg+1, multiple*i)
#     find_dif()
# print(min_dif)


#19637 if문 좀 대신 써줘 - 시간 초과
# import sys
#
# N, M = map(int, input().split())
# match = {}
# numbers = []
# new_input = sys.stdin.readline
# for _ in range(N):
#     name, number = new_input().split()
#     number = int(number)
#     match.setdefault(number, name)
#     if match[number] == name:
#         numbers.append(number)
# def alias(power):
#     for number in numbers:
#         if power <= number:
#             return match[number]
#
# for _ in range(M):
#     print(alias(int(new_input())))


# 이분 탐색
# import sys
# N, M = map(int, input().split())
# names = []
# numbers = []
# new_input = sys.stdin.readline
# for _ in range(N):
#     name, number = new_input().split()
#     names.append(name)
#     numbers.append(int(number))
# def alias(power):
#     start = 0
#     end = N-1
#     while start <= end:
#         mid = (start + end) // 2
#         if power == numbers[mid]:
#             return names[mid]
#         elif power < numbers[mid]:
#             if mid == 0:
#                 return names[0]
#             end = mid - 1
#         else:
#             start = mid + 1
#     return names[end]
#
# for _ in range(M):
#     print(alias(int(new_input())))
#0 weak 10000 normal 100000 strong 1000000


#2193 이친수
# N = int(input())
# numbers = ['1']
# cnt = 1
# if N != 1:
#     while True:
#         number = numbers.pop(0)
#         if len(number) == N:
#             numbers.append(number)
#             break
#         numbers.append(number + '0')
#         if number[-1] == '0':
#             numbers.append(number + '1')
#     cnt = len(numbers)
# print(cnt)


#1247 부호
# import sys
# new_input = sys.stdin.readline
# for _ in range(3):
#     N = int(new_input())
#     total = 0
#     for _ in range(N):
#         total += int(new_input())
#     answer = '0'
#     if total:
#         answer = ['+','-'][total < 0]
#     print(answer)
