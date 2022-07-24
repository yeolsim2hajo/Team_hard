# 백준 3273 두 수의 합

import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
lst.sort()
x = int(input())
ans, s, e = 0, 0, n-1
while s < e:
    if lst[s]+lst[e] == x:
        ans += 1
        s += 1
        e -= 1
    elif lst[s]+lst[e] > x:
        e -= 1
    else:
        s += 1
print(ans)