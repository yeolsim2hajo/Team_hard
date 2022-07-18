# 백준 17212 달나라 토끼를 위한 구매대금 지불 도우미

import sys
input = sys.stdin.readline
n = int(input())
if n == 3 or n%7 == 4 or n%7 == 6:
    print((n+13)//7)
else:
    print((n+6)//7)