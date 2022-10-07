# 백준 18512 점프 점프

import sys
input = sys.stdin.readline

x, y, p1, p2 = map(int, input().split())
ans = 0
while p1 != p2:
    if ans > 1000:
        p1 = -1
        break
    if p1 > p2:
        p2 += y
    else:
        p1 += x
    ans += 1
print(p1)