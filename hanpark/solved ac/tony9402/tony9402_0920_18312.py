# 백준 18312 시각

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a, b, c, rst = 0, 0, 0, 0
for a in range(n+1):
    if a < 10:
        a = '0' + str(a)
    for b in range(60):
        if b < 10:
            b = '0' + str(b)
        for c in range(60):
            if c < 10:
                c = '0' + str(c)
            if str(k) in str(a) or str(k) in str(b) or str(k) in str(c):
                rst += 1
print(rst)