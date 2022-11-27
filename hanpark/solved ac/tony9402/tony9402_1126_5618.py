# tony9402 5618 공약수

import sys
input = sys.stdin.readline

def abc(a, b):
    if(a == 0):
        return b
    return abc(b % a, a)
n = int(input())
lst = list(map(int, input().split()))
ans = abc(lst[0], abc(lst[1], lst[-1]))
for i in range(1, (ans // 2) + 1):
    if ans % i == 0:
        print(i)
print(ans)