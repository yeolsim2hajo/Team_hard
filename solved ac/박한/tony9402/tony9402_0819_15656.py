# 백준 15656 N과 M(7)

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
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