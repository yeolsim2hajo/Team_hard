#14501 퇴사
# import sys
#
# new_input = sys.stdin.readline
# N = int(new_input())
# schedule = []
# for _ in range(N):
#     schedule.append(list(map(int, input().split())))
# max_profit = schedule[0][0]
# path = []
# def dfs(start, profit):
#     global max_profit
#     for j in range(start, N):
#         day, money = schedule[j]
#         if start + day <= N:
#             max_profit = max(max_profit, profit+money)
#             dfs(start+day, profit+money)
#
#
#
# for i in range(N):
#     dfs(i+schedule[i][0], schedule[i][1])
# print(max_profit)


#10974 모든 순열
N = int(input())
visited = [False] * (N+1)
path = []
def dfs(arg):
    if arg == N:
        print(*path)
    for i in range(1,N+1):
        if visited[i] is False:
            visited[i] = True
            path.append(i)
            dfs(arg+1)
            path.pop()
            visited[i] = False
dfs(0)

