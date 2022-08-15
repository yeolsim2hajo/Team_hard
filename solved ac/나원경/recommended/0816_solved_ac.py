# import sys
#
# new_input = sys.stdin.readline
# N = int(new_input())
# tree = {}
# root = {}
# for _  in range(N):
#     key, *values = map(int, new_input().split())
#     tree[key] = values
#     for value in values:
#         if value != -1:
#             root[value] = key
# key = 1
# visited = {1}
# cnt = 0
# while len(visited) < N:
#     print(key)
#     cnt += 1
#     for i in range(2):
#         next = tree[key][i]
#         if next != -1 and next not in visited:
#             key = next
#             visited.add(key)
#             break
#     else:
#         key = root[key]
# print(cnt)

'''
15
1 2 3
2 4 5
3 6 7
4 8 9
5 10 11
6 12 13
7 14 15
8 -1 -1
9 -1 -1
10 -1 -1
11 -1 -1
12 -1 -1
13 -1 -1
14 -1 -1
15 -1 -1
'''

#4097 수익
# def calc_profit():
#     import sys
#     new_input = sys.stdin.readline
#     while True:
#         N = int(new_input())
#         if N == 0:
#             return
#         profit_list = [0]
#         for _ in range(N):
#             profit = int(new_input())
#             profit_list.append(profit_list[-1]+profit)
#         max_end, min_start = (profit_list[-1], N-1), (profit_list[0], 0)
#         start, end = 1, N-2
#         for _ in range(N-1):
#             if profit_list[start] < min_start[0] and start <= max_end[1]:
#                 min_start = (profit_list[start], start)
#             if profit_list[end] > max_end[0] and end >= min_start[1]:
#                 max_end = (profit_list[end], end)
#             start += 1
#             end -= 1
#         print(max_end[0]-min_start[0])
#
# calc_profit()

# 15650 N과 M
# N, M = map(int, input().split())
# path = []
# def dfs(arg=0, start=1):
#     if arg == M:
#         print(*path)
#         return
#     for i in range(start,N+1):
#         path.append(i)
#         dfs(arg+1, i+1)
#         path.pop()
# dfs()

# 메모리 별 차이 없고 시간 더 걸림
# N, M = map(int, input().split())
# path = []
# def dfs(arg, start):
#     if arg == M:
#         print(*path)
#         return
#     for i in range(start,N+1):
#         path.append(i)
#         dfs(arg+1, i+1)
#         path.pop()
# dfs(0,1)


N, M = map(int, input().split())
path = [0] * (N+1)
def dfs(arg=1, cnt=0):
    if cnt == M:
        for i in range(1,arg):
            if path[i]:
                print(i, end=' ')
        print()
        return
    if arg == N+1:
        return
    for i in range(1,-1,-1):
        path[arg] = i
        dfs(arg+1, cnt+i)
        path[arg] = 0

dfs()