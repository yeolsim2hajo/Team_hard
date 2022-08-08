# 백준 15650 N과 M(4)

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = [0]*n
for a in range(n):
    lst[a] = a+1
ans = []
def abc(level, check):
    if level == m:
        print(*ans)
        return
    for i in range(check, n):
        ans.append(lst[i])
        abc(level+1, i)
        ans.pop()
abc(0, 0)