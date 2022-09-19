# 백준 9375 패션왕 신해빈

'''
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    if n == 0:
        print(0)
        continue
    arr = [list(input().split()) for _ in range(n)]
    arr.sort(key=lambda x:x[1])
    rst, ans, m, a = 0, 1, 0, arr[0][1]
    lst = []
    while rst < n:
        if arr[rst][1] != a:
            a = arr[rst][1]
            lst.append(m)
            m = 1
        else:
            m += 1
        rst += 1
    if m > 1:
        lst.append(m)
    for i in range(len(lst)):
        ans *= (lst[i]+1)
    print(ans-1)
'''
from collections import Counter
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    lst = []
    for _ in range(n):
        a, b = input().split()
        lst.append(b)
    rst = Counter(lst)
    ans = 1
    for i in range(len(rst)):
        ans *= (rst[i]+1)
    print(ans-1)
