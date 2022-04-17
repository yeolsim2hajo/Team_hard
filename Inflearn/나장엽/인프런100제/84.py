number = list(input())
k = int(input())
n = int(input())

path = ['']*k
answer = []
used = [0]*n
def dfs(level):
    if level == k:
        result = ''
        for i in range(len(path)):
            result+=path[i]
        answer.append(result)
        return

    for i in range(n):
        if used[i] == 1: continue
        used[i] = 1
        path[level] = number[i]
        dfs(level+1)
        used[i] = 0



dfs(0)
answer = [int(i) for i in answer]
print(max(answer))