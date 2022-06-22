#9375 패션왕 신해빈
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     clothes = {}
#     length = 0
#     for _ in range(N):
#         name, kind = input().split()
#         if clothes.get(kind):
#             clothes[kind].append(name)
#         else:
#             clothes[kind] = [name]
#     print(clothes.keys())
#     def bfs():
#         from collections import deque
#         q = deque()
#         keys = list(clothes.keys())
#         q.append((keys[0],0))
#         case = q[0][0]
#         for i in range(1, len(keys)):
#             while q:
#                 , cnt = q.popleft()
#                 for x, y in clothes:
#                     if kind == y:
#                         q.append([x,y])
#                     else:
#                         q.append()
#             q.append(clothes[keys[i]])

# 시간 초과
# import sys
#
# T = int(input())
# new_input = sys.stdin.readline
# for _ in range(T):
#     N = int(input())
#     clothes = []
#     for _ in range(N):
#         clothes.append(new_input().split())
#     path_kind = set()
#     cnt = 0
#     def dfs(arg=0, start=0):
#         global cnt
#         if path_kind:
#             cnt += 1
#         for i in range(start,N):
#             kind = clothes[i][1]
#             if kind not in path_kind:
#                 path_kind.add(kind)
#                 dfs(arg+1, i+1)
#                 path_kind.remove(kind)
#     dfs()
#     print(cnt)


# dict + dfs
# import sys
#
# T = int(input())
# new_input = sys.stdin.readline
# for _ in range(T):
#     N = int(input())
#     clothes = {}
#     for _ in range(N):
#         name, kind = new_input().split()
#         clothes[name] = kind
#     path_kind = set()
#     path_name = set()
#     cnt = 0
#     keys = list(clothes.keys())
#     def dfs(arg=0, start=0):
#         global cnt
#         if path_name:
#             cnt += 1
#         for i in range(start, N):
#             key = keys[i]
#             if clothes[key] not in path_kind and key not in path_name:
#                 path_name.add(key)
#                 path_kind.add(clothes[key])
#                 dfs(arg+1, i+1)
#                 path_name.remove(key)
#                 path_kind.remove(clothes[key])
#     dfs()
#     print(cnt)

# dict + for
# import sys
#
# T = int(input())
# new_input = sys.stdin.readline
# for _ in range(T):
#     N = int(input())
#     clothes = {}
#     for _ in range(N):
#         name, kind = new_input().split()
#         clothes[name] = kind
#     cnt = 0
#     keys = list(clothes.keys())
#     answer = [[key] for key in keys]
#     for key in keys:
#         for element in answer:
#             if clothes[key] != clothes[element[0]]:
# import sys
#
# print(cnt)

#11652 카드
# import sys
# N = int(input())
# new_input = sys.stdin.readline
# cnt = {}
# for _ in range(N):
#     number = int(new_input())
#     if cnt.get(number):
#         cnt[number] += 1
#     else:
#         cnt[number] = 1
# max_val = 1
# max_key = 2**62
# for key, value in cnt.items():
#     if max_val < value:
#         max_val = value
#         max_key = key
#     elif max_val == value and max_key > key:
#         max_key = key
# print(max_key)


# list로 하면? - 메모리 차이 없음, 시간 차이 거의 없음
# import sys
# N = int(input())
# new_input = sys.stdin.readline
# cnt = {}
# for _ in range(N):
#     number = int(new_input())
#     if cnt.get(number):
#         cnt[number] += 1
#     else:
#         cnt[number] = 1
# max_list = [1,2**62]
# for key, value in cnt.items():
#     if max_list[0] < value:
#         max_list = [value, key]
#     elif max_list[0] == value and max_list[1] > key:
#         max_list[1] = key
# print(max_list[1])


#1302 베스트셀러
# N = int(input())
# book = {}
# for _ in range(N):
#     name = input()
#     book.setdefault(name, 0)
#     book[name] += 1
# best_seller = 'z'*50
# cnt = 1
# for key, value in book.items():
#     if cnt < value:
#         best_seller = key
#         cnt = value
#     elif cnt == value and best_seller > key:
#         best_seller = key
# print(best_seller)


# 기존 방법 - 크게 시간 차이가 나지 않음
# N = int(input())
# book = {}
# for _ in range(N):
#     name = input()
#     if book.get(name):
#         book[name] += 1
#     else:
#         book[name] = 1
# best_seller = 'z'*50
# cnt = 1
# for key, value in book.items():
#     if cnt < value:
#         best_seller = key
#         cnt = value
#     elif cnt == value and best_seller > key:
#         best_seller = key
# print(best_seller)


#7785 회사에 있는 사람
# 리스트 이용 - 시간 초과
# import sys
#
# N = int(input())
# people = []
# new_input = sys.stdin.readline
# for _ in range(N):
#     name, state = new_input().split()
#     if state == 'enter':
#         people.append(name)
#     elif name in people:
#         people.remove(name)
# people.sort(reverse=True)
# print(*people, sep='\n')


# set 이용
# import sys
#
# N = int(input())
# people = set()
# new_input = sys.stdin.readline
# for _ in range(N):
#     name, state = new_input().split()
#     if state == 'enter':
#         people.add(name)
#     elif name in people:
#         people.remove(name)
# print(*sorted(people, reverse=True), sep='\n')


#2776 암기왕
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     saw = set(map(int,input().split()))
#     M = int(input())
#     maybe = list(map(int,input().split()))
#     for number in maybe:
#         print(int(number in saw))

# int로 안 바꿈 - 시간 줄어듦
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     saw = set(input().split())
#     M = int(input())
#     maybe = input().split()
#     for number in maybe:
#         print(int(number in saw))

# deque 사용 - 메모리 약간 늘어남 + 시간 약간 줄어듦
# from collections import deque
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     saw = set(input().split())
#     M = int(input())
#     maybe = deque()
#     maybe.extend(input().split())
#     for _ in range(M):
#         print(int(maybe.popleft() in saw))
