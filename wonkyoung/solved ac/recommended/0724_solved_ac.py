# N = int(input())
# board = [list(map(str, input())) for _ in range(N)]
# swap_board = list(zip(*board))
# max_candy = 1
#
# def update_cnt(cnt):
#     global max_candy
#     if max_candy < cnt:
#         max_candy = cnt
# def count_horizontal():
#     global max_candy, board_cnt, swap_cnt
#     def exchange_candy(arr, choice):
#         nonlocal row, col
#         if choice == 0:
#             return 0
#         for dr in (-1,1):
#             if 0 <= row+dr < N and arr[row+dr][col] == arr[row][col]:
#                 return 1
#         return 0
#     for row in range(N):
#         if max_candy == N:
#             return
#         board_choice = swap_choice = 1
#         board_cnt = swap_cnt = 1
#         for col in range(N-1):
#             if board_cnt + (N-col) > max_candy:
#                 if board[row][col] == board[row][col+1]:
#                     board_cnt += 1
#                 elif exchange_candy(board, board_choice):
#                     board_cnt += 1
#                     board_choice -= 1
#                 else:
#                     update_cnt(board_cnt)
#                     board_choice = 1
#                 update_cnt(board_cnt)
#             if swap_cnt + (N - col) > max_candy:
#                 if swap_board[row][col] == swap_board[row][col+1]:
#                     swap_cnt += 1
#                 elif exchange_candy(swap_board, swap_choice):
#                     swap_cnt += 1
#                     swap_choice -= 1
#                 else:
#                     update_cnt(swap_cnt)
#                     swap_choice = 1
#                 update_cnt(swap_cnt)
# count_horizontal()
# print(max_candy)


#3273 두 수의 합
# N = int(input())
# numbers = set(map(int, input().split()))
# x = int(input())
# cnt = 0
# while numbers:
#     number = numbers.pop()
#     dif = x-number
#     if dif in numbers:
#         numbers.remove(dif)
#         cnt += 1
# print(cnt)

# discard가 시간 더 걸림
# N = int(input())
# numbers = set(map(int, input().split()))
# x = int(input())
# cnt = 0
# while numbers:
#     number = numbers.pop()
#     dif = x-number
#     if dif in numbers:
#         cnt += 1
#         numbers.discard(dif)
# print(cnt)


# 시간 더 걸림
# N = int(input())
# numbers = set(map(int, input().split()))
# x = int(input())
# cnt = 0
# while numbers:
#     number = numbers.pop()
#     dif = x-number
#     cnt = cnt+1 if dif in numbers else cnt
#     numbers.discard(dif)
# print(cnt)


# DAT 사용
# N = int(input())
# numbers = list(map(int, input().split()))
# check = [0] * 1000001
# for idx in numbers:
#     check[idx] = 1
# x = int(input())
# cnt = 0
# while numbers:
#     number = numbers.pop()
#     dif = x-number
#     if 0 <= dif <= 1e6 and check[dif]:
#         cnt += 1
# print(cnt//2)


#2중 for - 시간 초과
# N = int(input())
# numbers = list(map(int, input().split()))
# x = int(input())
# cnt = 0
# def find_dif():
#     global cnt
#     for j in range(i+1,N):
#         if dif == numbers[j]:
#             cnt += 1
#             return
#
# for i in range(N-1):
#     dif = x-numbers[i]
#     find_dif()
#
# print(cnt)


# 이분탐색 - 더 걸림
# N = int(input())
# numbers = sorted(list(map(int, input().split())))
# x = int(input())
# cnt = 0
#
# def find_dif():
#     global cnt
#     start = 0
#     end = N-2-i
#     while start <= end:
#         mid = (start + end)//2
#         if dif == numbers[mid]:
#             cnt += 1
#             return
#         if dif > numbers[mid]:
#             start = mid + 1
#         else:
#             end = mid - 1
#
# for i in range(N - 1):
#     dif = x - numbers.pop()
#     find_dif()
#
# print(cnt)


#1743 음식물 피하기 - 초기화 꼭 해주자
# import sys
# new_input = sys.stdin.readline
# N, M, K = map(int, input().split())
# position = {tuple(map(int, new_input().split())) for _ in range(K)}
# food = set()
# def find_max():
#     max_size = size = 1
#     while position:
#         y, x = position.pop()
#         for dy, dx in (-1,0), (1,0), (0,-1), (0,1):
#             ny, nx = y+dy, x+dx
#             if (ny,nx) in position:
#                 size += 1
#                 food.add((ny,nx))
#                 position.remove((ny,nx))
#         while food:
#             y, x = food.pop()
#             for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
#                 ny, nx = y + dy, x + dx
#                 if (ny, nx) in position:
#                     size += 1
#                     food.add((ny, nx))
#                     position.remove((ny, nx))
#         max_size = max(size, max_size)
#         size = 1
#     return max_size
# print(find_max())


# 코드 길이 줄이기 - 시간은 늘어남
# import sys
# new_input = sys.stdin.readline
# N, M, K = map(int, input().split())
# position = {tuple(map(int, new_input().split())) for _ in range(K)}
# def find_max():
#     food = set()
#     max_size = size = 1
#
#     def iter_set(target, option):
#         nonlocal size, max_size
#         while target:
#             y, x = target.pop()
#             for dy, dx in (-1,0), (1,0), (0,-1), (0,1):
#                 ny, nx = y+dy, x+dx
#                 if (ny,nx) in position:
#                     size += 1
#                     food.add((ny,nx))
#                     position.remove((ny,nx))
#             if option == 1:
#                 iter_set(food, 0)
#         if option == 0:
#             max_size = max(size, max_size)
#             size = 1
#
#     iter_set(position,1)
#     return max_size
# print(find_max())