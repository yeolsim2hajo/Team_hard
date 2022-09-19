# 백준 1166 선물

import sys
input = sys.stdin.readline
n, l, w, h = map(int, input().split())
rst, ans = 0, max(l, w, h)
for _ in range(1000):
    mid = (rst + ans)/2
    check = (l//mid)*(w//mid)*(h//mid)
    if check >= n:
        rst = mid
    else:
        ans = mid
print("%.10f" %(ans))
