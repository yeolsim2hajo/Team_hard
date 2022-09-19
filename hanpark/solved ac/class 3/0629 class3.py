# class 3++ 1697 숨바꼭질

#import sys
# input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())
lst = [0]*100001

def abc(n):
    q = deque()
    q.append(n)
    while q:
        m = q.popleft()
        if m == k:
            print(lst[k])
            break
        for i in (m*2, m+1, m-1):
            if 0 <= i <= 100000:
                if lst[i] != 0:
                    continue
                lst[i] = lst[m] + 1
                q.append(i)

abc(n)