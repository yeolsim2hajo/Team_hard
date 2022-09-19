# 백준 15654 N과 M (5)

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
ans = []
def abc(level):
    if level == m:
        print(*ans)
    for i in range(n):
        if lst[i] in ans:
            continue
        ans.append(lst[i])
        abc(level+1)
        ans.pop()
abc(0)