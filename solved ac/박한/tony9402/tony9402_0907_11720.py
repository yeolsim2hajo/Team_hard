# 백준 11720 숫자의 합

import sys
input = sys.stdin.readline
N = int(input())
lst = list(input().strip())
ans = 0
for a in lst:
    ans += int(a)
print(ans)