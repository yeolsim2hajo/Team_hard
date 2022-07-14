# 백준 2346 풍선 터뜨리기

from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque(enumerate(map(int, input().split())))
lst = []
while q:
    rst, a = q.popleft()
    lst.append(rst+1)
    if a > 0:
        q.rotate(-a+1)
    else:
        q.rotate(-a)
print(*lst)