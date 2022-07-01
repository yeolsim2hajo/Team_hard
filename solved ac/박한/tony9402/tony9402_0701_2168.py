# 백준 2168 타일 위의 대각선

import sys
input = sys.stdin.readline
x, y = map(int, input().split())
def abc(a, b):
    while b > 0:
        a, b = b, a%b
    return a

if x > y:
    print(x + y - abc(x, y))
else:
    print(x + y - abc(x, y))