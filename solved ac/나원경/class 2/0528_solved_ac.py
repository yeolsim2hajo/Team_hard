# import random
# print(random.choice(['프로파일러','살인정원']))

#18111 마인크래프트
# 시간 초과
# N, M, B = map(int,input().split())
# ground = []
# total = 0
# # max_height = 0
# # min_height = 256
# for _ in range(N):
#     ground.append(list(map(int, input().split())))
#     for element in ground[-1]:
#         total += element
#         # if max_height < element:
#         #     max_height = element
#         # if min_height > element:
#         #     min_height = element
# def grinding(ref):
#     global height, time
#     inventory = B
#     temp = 0
#     for i in range(N):
#         for j in range(M):
#             if ref < ground[i][j]:
#                 temp += (ground[i][j]-ref) * 2
#                 inventory += 1
#             elif ref > ground[i][j]:
#                 temp += (ref - ground[i][j])
#                 inventory -= 1
#             if time < temp:
#                 return
#     if inventory < 0:
#         return
#     elif time > temp:
#         time = temp
#         height = ref
#     elif ref > height:
#         height = ref
#
#
# average = round(total / (N * M))
# height = 0
# time = 1e8
# # 틀림
# for number in range(average-1, average+2):
#     grinding(average)
#
#
# # for number in range(max_height, min_height-1, -1):
# #     grinding(number)
# print(time, height)

# 시도
# N, M, B = map(int,input().split())
# ground = []
# check = {}
# max_val = 0
# min_val = 256
# for _ in range(N):
#     ground.append(list(map(int, input().split())))
#     for element in ground[-1]:
#         if max_val < element:
#             max_val = element
#         if min_val > element:
#             min_val = element
#         if check.get(element):
#             check[element] += 1
#         else:
#             check[element] = 1
#
# def grinding(ref):
#     global height, time
#     inventory = B
#     temp = 0
#     for key, value in check.items():
#         if key > ref:
#             temp += (key - ref) * value * 2
#             inventory += value
#         elif key < ref:
#             temp += (ref - key) * value
#             inventory -= value
#         if time < temp:
#             return
#     if inventory < 0:
#         return
#     elif time > temp:
#         time = temp
#         height = ref
#     elif ref > height:
#         height = ref
#
# height = 0
# time = 1e10
# for number in range(max_val, min_val-1, -1):
#     grinding(number)
#
# print(time, height)

#1018 체스판 다시 칠하기
chess = ['WBWBWBWB','BWBWBWBW']
N, M = map(int, input().split())
board = [input() for _ in range(N)]
def match(option):
    global min_cnt
    cnt = 0
    for row in range(i, i+8):
        if board[row][j:j+8] != chess[option]:
            for col in range(j, j+8):
                if board[row][col] != chess[option][col-j]:
                    cnt += 1
                if min_cnt <= cnt:
                    return
        option = 1-option
    min_cnt = cnt

min_cnt = 64
for i in range(N-7):
    for j in range(M-7):
        for k in range(2):
            match(k)
print(min_cnt)