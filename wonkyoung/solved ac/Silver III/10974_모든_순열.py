#220803
#
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

