#221010
# set 추가
# from collections import deque
# N = int(input())
# numbers = list(map(int, input().split()))
# def bfs(start):
#     order_by = deque([(start, [start])])
#     set_numbers = set(numbers)
#     while order_by:
#         now, result = order_by.popleft()
#         if len(result) < N:
#             multi = now*2
#             if now%3 == 0:
#                 div = now//3
#                 if div in set_numbers:
#                     order_by.append((div, [*result, div]))
#             if multi in set_numbers:
#                 order_by.append((multi, [*result, multi]))
#         elif len(result) == N:
#             if set(result) == set_numbers:
#                 return result
#
# for i in numbers:
#     if bfs(i):
#         print(*bfs(i))
#         break

# 처음부터 set으로 - 메모리 더 소요
# from collections import deque
# N = int(input())
# numbers = set(map(int, input().split()))
# def bfs(start):
#     order_by = deque([(start, [start])])
#     while order_by:
#         now, result = order_by.popleft()
#         if len(result) < N:
#             multi = now*2
#             if now%3 == 0:
#                 div = now//3
#                 if div in numbers:
#                     order_by.append((div, [*result, div]))
#             if multi in numbers:
#                 order_by.append((multi, [*result, multi]))
#         elif len(result) == N:
#             if set(result) == numbers:
#                 return result
#
# for i in numbers:
#     if bfs(i):
#         print(*bfs(i))
#         break


# dfs - 시간, 메모리 절약
# N = int(input())
# numbers = set(map(int, input().split()))
# def dfs(now, level=1):
#     global possible
#     if possible:
#         return
#     if level == N:
#         if set(new_numbers) == numbers:
#             possible = True
#             print(*new_numbers)
#         return
#     multi = now*2
#     if now%3 == 0:
#         div = now//3
#         if div in numbers:
#             new_numbers.append(div)
#             dfs(div, level+1)
#             new_numbers.pop()
#     if multi in numbers:
#         new_numbers.append(multi)
#         dfs(multi, level + 1)
#         new_numbers.pop()
#
# possible = False
# for i in numbers:
#     new_numbers = [i]
#     dfs(i)
#     if possible:
#         break


# dfs - if set 부분 없애기
# N = int(input())
# numbers = set(map(int, input().split()))
# def dfs(now, level=1):
#     global possible
#     if possible:
#         return
#     if level == N:
#         possible = True
#         print(*new_numbers)
#         return
#     multi = now*2
#     if now%3 == 0:
#         div = now//3
#         if div in numbers:
#             new_numbers.append(div)
#             dfs(div, level+1)
#             new_numbers.pop()
#     if multi in numbers:
#         new_numbers.append(multi)
#         dfs(multi, level + 1)
#         new_numbers.pop()
#
# possible = False
# for i in numbers:
#     new_numbers = [i]
#     dfs(i)
#     if possible:
#         break


# list를 인자로 - 시간, 메모리 같음
N = int(input())
numbers = set(map(int, input().split()))
def dfs(now, new_numbers, level=1):
    global possible
    if possible:
        return
    if level == N:
        possible = True
        print(*new_numbers)
        return
    multi = now*2
    if now%3 == 0:
        div = now//3
        if div in numbers:
            dfs(div, [*new_numbers, div], level+1)
    if multi in numbers:
        dfs(multi, [*new_numbers, multi], level + 1)

possible = False
for i in numbers:
    dfs(i, [i])
    if possible:
        break

# 바깥 함수
def calc():
    N = int(input())
    numbers = set(map(int, input().split()))

    def dfs(now, new_numbers, level=1):
        nonlocal possible
        if possible:
            return
        if level == N:
            possible = True
            print(*new_numbers)
            return
        multi = now * 2
        if now % 3 == 0:
            div = now // 3
            if div in numbers:
                dfs(div, [*new_numbers, div], level + 1)
        if multi in numbers:
            dfs(multi, [*new_numbers, multi], level + 1)

    possible = False
    for i in numbers:
        dfs(i, [i])
        if possible:
            return
calc()

