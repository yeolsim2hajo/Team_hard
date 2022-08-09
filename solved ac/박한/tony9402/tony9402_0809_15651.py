# 백준 15651 N과 M(3)

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = [0]*(n)
for a in range(n):
    lst[a] = a+1
ans = []
def abc(level):
    if level == m:
        print(*ans)
        return
    for i in range(n):
        ans.append(lst[i])
        abc(level+1)
        ans.pop()
abc(0)