# 백준 17179 케이크 자르기

import sys
input = sys.stdin.readline

N, M, L = map(int, input().strip().split())
lst = list(int(input().strip()) for _ in range(M))
lst.append(L)
def find(num):
    check, rst = 0, 0
    for i in range(M+1):
        if lst[i]-check >= num:
            check = lst[i]
            rst += 1
    if rst > n:
        return True
    else:
        return False
for _ in range(N):
    n = int(input())
    l, r, ans = 1, 4000000, 0
    while l <= r:
        m = (l+r)//2
        if find(m):
            l = m+1
            ans = max(m, ans)
        else:
            r = m-1
    print(ans)