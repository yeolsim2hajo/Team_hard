# 백준 22864 피로도

import sys
input = sys.stdin.readline

a, b, c, m = map(int, input().split())
rst, ans = 0, 0
for _ in range(24):
    if rst + a > m:
        if rst - c < 0:
            rst = 0
        else:
            rst -= c
    else:
        rst += a
        ans += b
print(ans)