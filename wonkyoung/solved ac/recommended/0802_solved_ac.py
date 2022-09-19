#15654
# N, M = map(int, input().split())
# arr = sorted(map(int, input().split()))
# path = []
# visited = [False] * N
# def dfs(arg):
#     if arg == M:
#         print(*path)
#         return
#     for i in range(N):
#         if visited[i] is False:
#             visited[i] = True
#             path.append(arr[i])
#             dfs(arg+1)
#             visited[i] = False
#             path.pop()
# dfs(0)


#11659 구간 합 구하기
# import sys
#
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# numbers = list(map(int, new_input().split()))
# acc = [0] + numbers[:]
# for i in range(2,N+1):
#     acc[i] += acc[i-1]
# for _ in range(M):
#     start, end = map(int, new_input().split())
#     print(acc[end] - acc[start-1])


# # 시간 더 걸림
# import sys
#
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# numbers = list(map(int, new_input().split()))
# acc = [0] + numbers[:1]
# for i in range(1,N):
#     acc.append(acc[i] + numbers[i])
# for _ in range(M):
#     start, end = map(int, new_input().split())
#     print(acc[end] - acc[start-1])


# 새 배열 만들지 않음
# import sys
#
# new_input = sys.stdin.readline
# N, M = map(int, input().split())
# numbers = [0] + list(map(int, input().split()))
# for i in range(2,N+1):
#     numbers[i] += numbers[i-1]
# for _ in range(M):
#     start, end = map(int, new_input().split())
#     print(numbers[end] - numbers[start-1])


import sys

new_input = sys.stdin.readline
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
for i in range(1,N):
    numbers[i] += numbers[i-1]
for _ in range(M):
    start, end = map(int, new_input().split())
    start = start-2 if start > 1 else start-1
    end = end-1 if end > 1 else end
    print(numbers[end] - numbers[start])