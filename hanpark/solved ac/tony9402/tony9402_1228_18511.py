# 백준 18511 큰 수 구성하기

import sys
input = sys.stdin.readline

n, k = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort(reverse=True)
ans = 0
def find(a, b):
    global ans
    if a == len(str(n)):
        if not '0' in str(b):
            ans = max(ans, b)
        return
    for i in range(k):
        c = lst[i]*(10**(len(str(n))-a-1)) + b
        if c > n:
            find(a+1, b)
        else:
            find(a+1, c)
find(0, 0)
print(ans)