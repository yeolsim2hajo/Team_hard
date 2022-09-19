# 백준 11726 2xn 타일링

import sys
input = sys.stdin.readline
n = int(input())
a, b = 2, 1
if n < 2:
    print(b)
else:
    for _ in range(n-2):
        a, b = a+b, a
    print(a%10007)