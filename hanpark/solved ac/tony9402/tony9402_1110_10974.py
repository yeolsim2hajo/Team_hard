# 백준 10974 모든 순열

n = int(input())
lst = []
def dfs():
    if len(lst) == n:
        print(*lst)
        return
    for i in range(1, n+1):
        if i not in lst:
            lst.append()
            dfs()
            lst.pop()
dfs()