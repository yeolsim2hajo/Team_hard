# 백준 16206 롤케이크

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().strip().split())
lst = list(map(int, input().strip().split()))
lst.sort(key=lambda x: (x%10, x))
ans = 0
for i in range(len(lst)):
    rst = lst[i]//10
    if lst[i]%10:
        if rst > m:
            ans += m
            m -= m
        else:
            ans += rst
            m -= rst
    else:
        if rst-1 > m:
            ans += m
            m -= m
        else:
            ans += rst
            m -= rst-1
print(ans)

# lambda 활용해서 정렬해주기
# case by case를 나눠서 각각 연산해주기