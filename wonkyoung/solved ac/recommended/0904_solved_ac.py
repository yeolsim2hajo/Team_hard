#14575 뒤풀이
# N, T = map(int, input().split())
# alcohol = []
# S = -1
# total = 0
# for _ in range(N):
#     alcohol.append(list(map(int, input().split())))
#     total += alcohol[-1][0]
#     S = max(S, alcohol[-1][0])
# if total < T:
#     average, remain = divmod(T, N)
#     S, total = average, average * N
#     left_dif, right_dif = [], []
#     left_dif_sum = right_dif_sum = 0
#     while True:
#         for left, right in alcohol:
#             if S >= left:
#                 left_dif.append(S - left)
#             else:
#                 left_dif.append(0)
#                 total -= (S-left)
#             if S <= right:
#                 right_dif.append(right - S)
#             else:
#                 right_dif.append(0)
#                 total += (right - S)
#             left_dif_sum += left_dif[-1]
#             right_dif_sum += right_dif[-1]
#         if total > T:
#             if S == -1:
#                 pass
#             else:
#                 break
#         elif total < T:
#             if S == -1:
#                 pass
#             else:
#                 break
#         else:
#             average = S
#             S -= 1
#             total = S * N
#     S = average
# elif total > T:
#     S = -1
# print(S)



#1159 농구 경기
# N = int(input())
# alp = {chr(ord('a')+i):0 for i in range(26)}
# for _ in range(N):
#     first = input()[0]
#     alp[first] += 1
# answer = ''
# if N >= 5:
#     for key, value in alp.items():
#         if value >= 5:
#             answer += key
# if answer == '':
#     answer = 'PREDAJA'
# print(answer)


# 시간 덜 걸림
# N = int(input())
# alp = {chr(ord('a')+i):0 for i in range(26)}
# for _ in range(N):
#     first = input()[0]
#     alp[first] += 1
# answer = ''
# for key, value in alp.items():
#     if value >= 5:
#         answer += key
# if answer == '':
#     answer = 'PREDAJA'
# print(answer)

# 시간 별 차이 없음
# N = int(input())
# alp = {chr(ord('a')+i):0 for i in range(26)}
# for _ in range(N):
#     first = input()[0]
#     alp[first] += 1
# answer = ''
# for key in alp.keys():
#     if alp[key] >= 5:
#         answer += key
# if answer == '':
#     answer = 'PREDAJA'
# print(answer)

# 시간 더 걸림
# def find_answer():
#     N = int(input())
#     alp = {chr(ord('a')+i):0 for i in range(26)}
#     for _ in range(N):
#         first = input()[0]
#         alp[first] += 1
#     if N >= 5:
#         answer = ''
#         for key in alp.keys():
#             if alp[key] >= 5:
#                 answer += key
#         return answer if answer else 'PREDAJA'
#     return 'PREDAJA'
# print(find_answer())


# def find_answer():
#     N = int(input())
#     alp = {chr(ord('a')+i):0 for i in range(26)}
#     for _ in range(N):
#         first = input()[0]
#         alp[first] += 1
#     answer = ''
#     for key in alp.keys():
#         if alp[key] >= 5:
#             answer += key
#     return answer if answer else 'PREDAJA'
# print(find_answer())