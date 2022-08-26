#15652 N과 M
# N, M = map(int, input().split())
# path = []
# def dfs(arg=0, start=1):
#     if arg == M:
#         print(*path)
#         return
#     for i in range(start, N+1):
#         path.append(i)
#         dfs(arg+1, i)
#         path.pop()
# dfs()



# N, M = map(int, input().split())
# def dfs(arg=0, start=1, path=''):
#     if arg == M:
#         print(path.rstrip())
#         return
#     for i in range(start, N+1):
#         dfs(arg+1, i, path+str(i)+' ')
# dfs()