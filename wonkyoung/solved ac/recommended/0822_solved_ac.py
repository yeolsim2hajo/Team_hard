#1264 모음의 개수
# def cnt():
#     import sys
#     new_input = sys.stdin.readline
#     vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
#     while True:
#         S = new_input().rstrip()
#         if S == '#':
#             return
#         total = 0
#         for alp in S:
#             if alp in vowel:
#                 total += 1
#         print(total)
# cnt()




# for _ in range(10):
#     T = int(input())
#     puzzle = [input() for _ in range(100)]
#     max_cnt = 1
#     # 행
#     for i in range(100):
#         left, right = 0, 99
#         for j in range(100-max_cnt):
#             if puzzle[i][left] == puzzle[i][right] and right - left >= max_cnt:
#                 cnt = 2
#                 while left < right:
#                     left += 1
#                     right -= 1
#                     if puzzle[i][left] == puzzle[i][right]:
#                         cnt += 2
#                     else:
#                         cnt = 0
#                         left = j
#                         break
#                 else:
#                     if left == right:
#                         cnt += 1
#                     max_cnt = max(max_cnt, cnt)
#                     break
#             else:
#                 right -= 1
#     # 열
#     for i in range(100):
#         left, right = 0, 99
#         for j in range(100-max_cnt):
#             if puzzle[left][i] == puzzle[right][i] and right - left >= max_cnt:
#                 cnt = 2
#                 while left < right:
#                     left += 1
#                     right -= 1
#                     if puzzle[left][i] == puzzle[right][i]:
#                         cnt += 2
#                     else:
#                         cnt = 0
#                         left = j
#                         break
#                 else:
#                     if left == right:
#                         cnt += 1
#                     max_cnt = max(max_cnt, cnt)
#                     break
#             else:
#                 right -= 1
#     print(f'#{T} {max_cnt}')

