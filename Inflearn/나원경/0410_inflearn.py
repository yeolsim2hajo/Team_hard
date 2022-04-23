# #94 LRU 알고리즘
# page_frame = int(input()) # 페이지 프레임 수
# pages = input() # 페이지
# memory = ['']*page_frame # 메모리
# check = [0]*page_frame # 사용된 횟수
# length = len(pages) # 총 페이지 수
# page_i = memory_i = 0 # 인덱스
# result_time = 0 # 실행 시간
# if page_frame:
#     while page_i < length:
#         # 메모리에 페이지가 있을 경우 check에 사용 횟수 추가, 실행 시간 1초
#         if pages[page_i] in memory:
#             check[memory.index(pages[page_i])] += 1
#             result_time += 1
#         # 메모리에 페이지가 없을 경우 메모리 갱신
#         else:
#             # 현재 메모리의 인덱스의 check 값이 최소가 아니면 최소인 인덱스로 이동
#             min_val = min(check)
#             if check[memory_i] != min_val:
#                 memory_i = check.index(min_val)
#             # 덮어씌우는 것이므로 check에서의 값 초기화, 실행 시간 6초
#             check[memory_i] = 0
#             result_time += 6
#         # 메모리에 값을 집어넣고 메모리와 페이지 인덱스 이동 - 공통
#         memory[memory_i] = pages[page_i]
#         memory_i += 1
#         page_i += 1
#         if memory_i >= page_frame:
#             memory_i = 0
# else:
#     result_time = length*6
# print(result_time)
'''
3
bcbaebce

3
abcabcabc

0
abcdef
'''

#96 넓은 텃밭 만들기 - 다시
# def dfs(y, x):
#     global possible
#     if x == j+n-1:
#         if bat[y][x] == '0':
#             if y == i + n - 1:
#                 possible = True
#                 return
#             x = 0
#             y += 1
#         else:
#             return
#
#     if bat[y][x+1] == '0':
#         bat[y][x + 1] = '#'
#         dfs(y,x+1)
#     else:
#         return
#
# ground = []
# bat = []
# for i in range(5):
#     ground.append(input('텃밭을 입력하세요 : ').split())
#     bat.append(ground[i][:])
# possible = False
# for n in range(5, -1, -1):
#     for i in range(5 - n + 1):
#         for j in range(5 - n + 1):
#             if bat[i][j] == '0':
#                 bat[i][j] = '#'
#                 dfs(i,j)
#                 bat = [ground[i][:] for i in range(5)]
#             if possible:
#                 print(f'{n} X {n}')
#                 break
#         if possible:
#             break
#     if possible:
#         break
# # print(*ground)
# # for i in range(5):
# #     print(*bat[i])
# '''
# 0 0 0 0 0
# 0 1 0 0 0
# 0 1 0 0 0
# 0 0 1 0 0
# 0 0 0 1 0
# '''