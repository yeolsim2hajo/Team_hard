# 백준 7795 먹을 것인가 먹힐 것인가

import sys
input = sys.stdin.readline
import bisect

for _ in range(int(input())):
    n, m = map(int, input().split())
    lst1 = sorted(list(map(int, input().split())))
    lst2 = sorted(list(map(int, input().split())))
    ans = 0
    for l in lst1:
        ans += (bisect.bisect(lst2, l-1))
    print(ans)