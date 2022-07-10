#19948 음유시인 영재
# poet = input().split()
# space = int(input())
# keyboard = list(map(int, input().split()))
# def typing():
#     piece = len(poet)
#     if piece - 1 > space:
#         return -1
#     cnt = {chr(65+i):keyboard[i] for i in range(26)}
#     answer = ''
#
#     def possible(word, end):
#         nonlocal pre
#         for i in range(1, end):
#             alp = word[i]
#             if pre == alp:
#                 continue
#             pre = alp
#             alp = alp.upper()
#             if cnt[alp] <= 0:
#                 return 0
#             cnt[alp] -= 1
#         return 1
#
#     for element in poet:
#         pre = element[0]
#         answer += pre.upper()
#         if cnt[answer[-1]]:
#             cnt[answer[-1]] -= 1
#             ret = possible(element, len(element))
#         else:
#             return -1
#         if ret == 0:
#             return -1
#
#     pre = answer[0]
#     if cnt[pre]:
#         cnt[pre] -= 1
#         ret = possible(answer, piece)
#         if ret == 0:
#             return -1
#         return answer
#     return -1
#
# print(typing())



# 0부터 &  함수 안의 함수 x
# poet = input().split()
# space = int(input())
# keyboard = list(map(int, input().split()))
# def typing():
#     piece = len(poet)
#     if piece - 1 > space:
#         return -1
#     cnt = {chr(65+i):keyboard[i] for i in range(26)}
#     answer = ''
#
#     for element in poet:
#         pre = ''
#         for i in range(len(element)):
#             alp = element[i]
#             if pre == alp:
#                 continue
#             alp = alp.upper()
#             if cnt[alp] <= 0:
#                 return -1
#             if i == 0:
#                 answer += alp
#             cnt[alp] -= 1
#             pre = alp
#
#     pre = ''
#     for alp in answer:
#         if pre == alp:
#             continue
#         if cnt[alp] <= 0:
#             return -1
#         cnt[alp] -= 1
#         pre = alp
#     return answer
#
# print(typing())


#Cup - A - 런타임 에러
# N, K = map(int, input().split())
# height = list(map(int, input().split()))
# div = 1e9 + 7
# cnt = 0
# visited = [False] * N
# path = []
# def choose(arg=0):
#     global cnt
#     if arg == K:
#         for i in range(K):
#
#         cnt += 1
#         return
#     for i in range(N):
#         if visited[i] is False:
#             visited[i] = True
#             path.append(height[i])
#             choose(arg+1)
#             visited[i] = False
#             path.pop()
#
# # def factorial(number):
# #     if number <= 1:
# #         return 1
# #     return number * factorial(number-1)
#
# if K <= 1:
#     cnt = N * K
# else:
#     cnt =
# print(int(cnt%div))


# Cup - B - 시간 초과
# N = int(input())
# A = list(map(int, input().split()))
# def find_mex():
#     global temp
#     import heapq
#     max_val = int(1e9)
#     heapq.heapify(temp)
#     min_number = heapq.heappop(temp)
#     for i in range(max_val):
#         if i < min_number:
#             return i
#         if temp:
#             min_number = heapq.heappop(temp)
#         else:
#             return min_number + 1
# def fill_lst(lst):
#     global temp
#     answer = []
#     temp = lst[:]
#     answer.append(find_mex())
#     for i in range(N):
#         temp = lst[:]
#         temp.pop(i)
#         answer.append(find_mex())
#     return answer
#
# B = list(set(fill_lst(A)))
# C = list(set(fill_lst(B)))
# temp = C
# print(find_mex())


# 시간 초과
# N = int(input())
# A = set(map(int, input().split()))
# def find_mex():
#     global temp
#     import heapq
#     max_val = int(1e9)
#     heapq.heapify(temp)
#     min_number = heapq.heappop(temp)
#     for i in range(max_val):
#         if i < min_number:
#             return i
#         if temp:
#             min_number = heapq.heappop(temp)
#         else:
#             return min_number + 1
# def fill_set(old_set):
#     global temp
#     answer = set()
#     temp = list(old_set)
#     answer.add(find_mex())
#     for i in range(N):
#         temp = list(old_set)
#         temp.pop(i)
#         answer.add(find_mex())
#     return answer
#
# B = fill_set(A)
# C = fill_set(B)
# temp = list(C)
# print(find_mex())


# 간소화 - 시간 초과
# N = int(input())
# A = set(map(int, input().split()))
# def fill_set(old_set, option=0):
#     global temp
#     max_val = int(1e9)
#     for i in range(max_val):
#         if i not in old_set:
#             mex = i
#             break
#     if option:
#         return mex
#
#     answer = {mex}
#     for i in range(N):
#         temp = list(old_set)
#         element = temp.pop(i)
#         if element < mex:
#             answer.add(element)
#     return answer
#
# B = fill_set(A)
# C = fill_set(B)
# print(fill_set(C,1))
