# 백준 11365 !밀비 급일

import sys
input = sys.stdin.readline
while 1:
    a = input().strip()
    if a == "END":
        break
    A, lenA = list(a), len(a)
    for i in range(lenA-1, -1, -1):
        print(A[i], end="")
    print()
