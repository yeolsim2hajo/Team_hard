# my_dictionary = {'possible':True}
# print(my_dictionary['possible'])

#18111 마인크래프트
# N, M, B = map(int,input().split())
# ground_cnt = [0]*257
# total = 0
# for _ in range(N):
#     ground = list(map(int,input().split()))
#     for j in range(M):
#         idx = ground[j]
#         ground_cnt[idx] += 1
#         total += idx
# min_time = 1e10
# ground_height = avg = total// (N*M)
# max_height = min((total+B)//(N*M), 256)
# for height in range(avg,max_height+1):
#     time = 0
#     inventory = B
#     for i in range(257):
#         if min_time < time:
#             break
#         if ground_cnt[i]:
#             if i > height:
#                 time += 2*(i-height) * ground_cnt[i]
#                 inventory += (i-height) * ground_cnt[i]
#             elif i < height:
#                 if inventory >= ground_cnt[i]:
#                     time += (height-i) * ground_cnt[i]
#                     inventory -= (height-i) * ground_cnt[i]
#                 else:
#                     break
#     else:
#         if time < min_time:
#             min_time = time
#             ground_height = height
#         elif ground_height > height:
#             ground_height = height
# print(min_time,ground_height)

#1018 체스판 다시 칠하기
# N, M = map(int,input().split())
# board = [input() for _ in range(N)]
# check = {'WBWBWBWB': True, 'BWBWBWBW': False}
# min_val = 64
#
# def chess(y,x):
#     start = check.get(board[y][x:x:8], -1)
#
#     else:
#     val = 0
#     for i in range(y,y+8):
#         for j in range(x, x+8):
#             if min_val < val:
#                 return
#
# for i in range(N-8):
#     for j in range(M-8):
#         chess(i,j)


#1436 영화감독 숌
# N = int(input())
# series = '666'
# if N == 1:
#     print(series)
# else:
#     plus = 0
#     cnt = 1
#     while cnt < N:
#         plus += 1
#         if '6' in str(plus):
#
#     print(series)

#1654 랜선 자르기
# K, N = map(int,input().split())
# lines = [int(input()) for _ in range(K)]
# if K == N:
#     print(min(lines))
# else:
#     max_length = sum(lines) // N
#
#     for length in range(max_length, 0, -1):
#         cnt = sum([line//length for line in lines])
#         if cnt >= N:
#             break
#     print(length)

#1874 스택 수열
# N = int(input())
# stack = []
# calc = []
# start = 1
# possible = True
# for _ in range(N):
#     number = int(input())
#     if possible:
#         for i in range(start,1+N):
#             if stack and stack[-1] == number:
#                 calc.append('-')
#                 stack.pop()
#                 break
#             calc.append('+')
#             stack.append(i)
#             if i == number:
#                 start = i+1
#                 calc.append('-')
#                 stack.pop()
#                 break
#         else:
#             if stack[-1] != number:
#                 possible = False
#             else:
#                 calc.append('-')
#                 stack.pop()
#
# if possible:
#     print(*calc, sep='\n')
# else:
#     print('NO')


