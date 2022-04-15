Str = list(input().split())
n = int(input())
path=['']*n
used = [0]*len(Str)
answer = []

def dfs(level, start):
    if level == n:
        for i in range(len(path)):
            print(path[i], end=' ')
        print()
        return


    for i in range(start, len(Str)):
        path[level] = Str[i]
        dfs(level+1, i+1)

dfs(0, 0)