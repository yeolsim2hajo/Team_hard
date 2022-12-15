# 백준 5014 스타트링크

import sys
input = sys.stdin.readline
from collections import deque

f, s, g, u, d = map(int, input().split())
def bfs(start):
    q = deque([])
    q.append((start, 0))
    lst = [0] * (f+1)
    lst[start] = 1
    while q:
        num, ans = q.popleft()
        if num == g:
            return ans
        for i in ('u', 'd'):
            new = num + u if i == 'u' else num - d
            if 1 <= new <= f and not lst[new]:
                q.append((new, ans + 1))
                lst[new] = 1
    return "use the stairs"
print(bfs(s))