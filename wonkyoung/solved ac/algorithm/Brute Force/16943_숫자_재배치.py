#221013 - 틀림
# A, B = input().split()
# A = sorted(map(str, A), reverse=True)
# int_A = list(map(int, A))
# answer = -1
# ref = int(B)
# length = len(A)
#
# def dfs(level, number):
#     global answer
#     if answer != -1:
#         return
#     if level == length:
#         number = int(number)
#         if number < ref:
#             answer = max(answer, number)
#         return
#     for j in range(length):
#         if visited[j] == 0:
#             visited[j] = 1
#             dfs(level+1, number + A[j])
#             visited[j] = 0
#
# visited = [0] * length
# for i in range(length):
#     if int_A[i]:
#         if A[i] <= B[0]:
#             visited[i] = 1
#             dfs(1, A[i])
#             if answer != -1:
#                 break
#             visited = [0] * length
#     else:
#         break
#
# print(answer)


#230131
# A, B = input().split()
# sorted_a = sorted(A, reverse=True)
# length_b, length_a = len(B), len(A)
# visited = [False] * length_a
# int_B = int(B)
# found = False
# max_val = -1
# def find_c(level=0, number=''):
#     global max_val, found
#     if found:
#         return
#     if level == length_a:
#         if number[0] == '0':
#             return
#         int_num = int(number)
#         if int_B > int_num:
#             max_val = int_num
#             found = True
#         return
#     for i in range(length_a):
#         if not visited[i]:
#             visited[i] = True
#             find_c(level+1, number + sorted_a[i])
#             visited[i] = False
# find_c()
# print(max_val)


# 가지 치기 => 시간 더 걸림
# A, B = input().split()
# sorted_a = sorted(A, reverse=True)
# length_b, length_a = len(B), len(A)
# visited = [False] * length_a
# int_B = int(B)
# found = False
# max_val = -1
# def find_c(level=0, number=''):
#     global max_val, found
#     if found:
#         return
#     if level == length_a:
#         if number[0] == '0':
#             return
#         int_num = int(number)
#         if int_B > int_num:
#             max_val = int_num
#             found = True
#         return
#     for i in range(length_a):
#         if not visited[i]:
#             visited[i] = True
#             find_c(level+1, number + sorted_a[i])
#             visited[i] = False
# if B[0] >= sorted_a[-1]:
#     find_c()
# print(max_val)

# 길이 조건 추가
# A, B = input().split()
# sorted_a = sorted(A, reverse=True)
# length_b, length_a = len(B), len(A)
# visited = [False] * length_a
# int_B = int(B)
# found = False
# max_val = -1
# def find_c(level=0, number=''):
#     global max_val, found
#     if found:
#         return
#     if level == length_a:
#         if number[0] == '0':
#             return
#         int_num = int(number)
#         if int_B > int_num:
#             max_val = int_num
#             found = True
#         return
#     for i in range(length_a):
#         if not visited[i]:
#             visited[i] = True
#             find_c(level+1, number + sorted_a[i])
#             visited[i] = False
# if length_a <= length_b:
#     find_c()
# print(max_val)


# 반복문
# A, B = input().split()
# length_b, length_a = len(B), len(A)
# sorted_a = sorted(A, reverse=True)
# visited = [False] * length_a
# int_B = int(B)
# found = False
# max_val = -1
# if length_a < length_b:
#     print(''.join(sorted_a))
# elif length_a == length_b:
#     sorted_by_close = [sorted(sorted_a, key=lambda num: num - B[i] if B[i] >= num else B[i] - num) for i in range(length_b)]
#     for first in sorted_by_close:
#         if first > B[0]:
#             break
#         elif first:
#             new_num = first
#             for i in range(1, length_b):
#


#230210
# A, B = input().split()
# length_a, length_b = len(A), len(B)
# if length_a > length_b:
#     print(-1)
# elif length_a < length_b:
#     print(''.join(sorted(A, reverse=True)))
# else:
#     C = ''
#     visited = [False] * length_a
#
#     def dfs(level, new):
#         global C
#         if level == length_a:
#             if C < new < B:
#                 C = new
#             return
#         for j in range(length_a):
#             if not visited[j]:
#                 visited[j] = True
#                 dfs(level+1, new+A[j])
#                 visited[j] = False
#
#     for i in range(length_a):
#         num = A[i]
#         if num != '0' and num <= B[0]:
#             visited[i] = True
#             dfs(1, A[i])
#             visited[i] = False
#     if C == '':
#         C = -1
#     print(C)


#
# def find_num():
#     A, B = input().split()
#     length_a, length_b = len(A), len(B)
#     if length_a > length_b:
#         return -1
#     elif length_a < length_b:
#         return ''.join(sorted(A, reverse=True))
#
#     visited = [False] * length_a
#     C = ''
#
#     def dfs(level, new):
#         nonlocal C
#         if level == length_a:
#             if C < new < B:
#                 C = new
#             return
#         for j in range(length_a):
#             if not visited[j]:
#                 visited[j] = True
#                 dfs(level+1, new+A[j])
#                 visited[j] = False
#
#     for i in range(length_a):
#         num = A[i]
#         if num != '0' and num <= B[0]:
#             visited[i] = True
#             dfs(1, A[i])
#             visited[i] = False
#     if C == '':
#         return -1
#     return C
# print(find_num())


# bfs - 틀림
# def find_num():
#     from collections import deque
#     A, B = input().split()
#     length_a, length_b = len(A), len(B)
#     sorted_a = sorted(A, reverse=True)
#     max_num = ''.join(sorted_a)
#     if length_a > length_b:
#         return -1
#     if length_a < length_b or max_num < B:
#         return max_num
#     visited = [False] * length_a
#     C = ''
#     q = deque()
#     for i in range(length_a):
#         num = sorted_a[i]
#         if num != '0' and num <= B[0]:
#             visited[i] = True
#             q.append((num, visited[:], 1))
#             while q:
#                 new, contain, length_c = q.popleft()
#                 if length_c == length_a:
#                     if C < new < B:
#                         C = new
#                     continue
#                 for j in range(length_a):
#                     if not contain[j]:
#                         contain[j] = True
#                         q.append((new+sorted_a[j], contain[:], length_c+1))
#     return C or -1
#
# print(find_num())



