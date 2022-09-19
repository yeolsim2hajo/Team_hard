# 백준 11663 선분 위의 점

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
def abc(k):
    s, e = 0, n-1
    while s <= e:
        mid = (s+e)//2
        if lst[mid] >= k:
            e = mid - 1
        else:
            s = mid + 1
    return e + 1
def bcd(k):
    s, e = 0, n-1
    while s <= e:
        mid = (s+e)//2
        if lst[mid] <= k:
            s = mid + 1
        else:
            e = mid - 1
    return e
for _ in range(m):
    a, b = map(int, input().split())
    rst = bcd(b)-abc(a)+1
    print(rst)