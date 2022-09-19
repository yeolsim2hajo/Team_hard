# class 3++ 1927 최소 힙

import sys
import heapq

input = sys.stdin.readline
n = int(input())
lst = []
for _ in range(n):
    m = int(input())
    if m > 0:
        heapq.heappush(lst, m)
    else:
        if lst == []:
            print(0)
        else:
            print(heapq.heappop(lst))