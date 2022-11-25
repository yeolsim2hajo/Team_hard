# tony9402 9046 복호화

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    lst = [0]*26
    L = list(input().strip())
    for l in L:
        if ord('a') <= ord(l) <= ord('z'):
            lst[ord(l)-ord('a')] += 1
    ans = 0
    for ls in range(len(lst)):
        if lst[ls] == max(lst):
            if ans != 0:
                ans = "?"
            else:
                ans = chr(ord('a')+ls)
    print(ans)