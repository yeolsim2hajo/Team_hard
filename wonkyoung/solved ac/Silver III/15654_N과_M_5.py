#220802
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