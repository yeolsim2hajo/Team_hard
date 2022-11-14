# 백준 13702 이상한 술집

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = [int(input()) for _ in range(n)]
s, e = 1, max(lst)
def binary(mid):
    total = 0
    for l in lst:
        total += (l // mid)
    return k <= total
ans = 0
while s <= e:
    m = (s + e) // 2
    if binary(m):
        ans = m
        s = m + 1
    else:
        e = m - 1
print(ans)