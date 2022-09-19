#
# N, K = map(int, input().split())
# height = list(map(int, input().split()))
# def choose(arg=0):
#     global cnt
#     if arg == K:
#         cnt += 1
#         return
#     for i in range(N):
#         if visited[i] is False:
#             path.append(height[i])
#             if arg > 1 and path[arg-1] < path[arg-2] and path[arg-1] < path[arg]:
#                 path.pop()
#                 continue
#             visited[i] = True
#             choose(arg+1)
#             visited[i] = False
#             path.pop()
#
# div = 1e9 + 7
# if K <= 2:
#     cnt = N * K
# else:
#     visited = [False] * N
#     path = []
#     cnt = 0
#     choose()
# print(int(cnt%div))


#1503 세 수 고르기
# N, M = map(int, input().split())
# if M:
#     S = set(map(int, input().split()))
#     not_in = {i for i in range(1,1001) if i not in S}
#     answer = 1e9
#     def find_answer():
#         global answer
#         for x in not_in:
#             number = x
#             if answer < abs(N - number):
#                 return
#             for y in not_in:
#                 number *= y
#                 if answer < abs(N - number):
#                     break
#                 for z in not_in:
#                     number *= z
#                     if answer < abs(N-number):
#                         break
#                     answer = abs(N-x*y*z)
#     find_answer()
# else:
#     answer = 0
# print(answer)


#19637 if문 좀 대신 써줘 - 시간 초과 (정렬 안 해도 시간 초과)
# import sys
# N, M = map(int, input().split())
# name = {}
# new_input = sys.stdin.readline
# for _ in range(N):
#     value, key = new_input().split()
#     name.setdefault(int(key), value)
# key_asc = sorted(name.keys())
# for _ in range(M):
#     power = int(new_input())
#     for key in key_asc:
#         if power <= key:
#             print(name[key])
#             break

# 시간 초과
# import sys
# N, M = map(int, input().split())
# name = {}
# keys = []
# new_input = sys.stdin.readline
# for _ in range(N):
#     value, key = new_input().split()
#     new_val = name.setdefault(int(key), value)
#     if new_val == value:
#         keys.append(int(key))
#
# def find_name():
#     for key in keys:
#         if power <= key:
#             return name[key]
#
# for _ in range(M):
#     power = int(new_input())
#     print(find_name())


#1935 후위 표기식2
# N = int(input())
# formula = input()
# match = {chr(65+i):int(input()) for i in range(N)}
# stack = []
# four = {'+', '-', '*', '/'}
# for element in formula:
#     if element not in four:
#         stack.append(match[element])
#     else:
#         second = stack.pop()
#         first = stack.pop()
#         if element == '+':
#             stack.append(first+second)
#         elif element == '-':
#             stack.append(first-second)
#         elif element == '*':
#             stack.append(first*second)
#         else:
#             stack.append(first/second)
# print(f'{stack[0]:.2f}')


# new_input 사용 - 시간 더 걸림