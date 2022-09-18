# 최소 시간 출력
# BFS
# x - 1, x + 1, 2 * x -> 세번 BFS 돌려서 찾는 시간을...?
# import sys
# from collections import deque
# input = sys.stdin.readline


# def bfs(n):
#     que = deque([n])
#     while que:
#         n = que.popleft()
#         if n == k:
#             return visited[n]

#         for i in (n-1, n+1, 2*n): # 수빈이가 서 있는 곳에서 -1, +1 * 2 인 위치들을 que에 넣고 확인.
#             if 0 <= i <= 100000  and not visited[i]: # 범위 안에 있고, 방문하지 않았다면...!
#                 visited[i] = visited[n] + 1 # 따로 cnt 변수 선언할 필요없이..1씩 증가시켜서 초 체크
#                 que.append(i)


# n, k = map(int, input().split())
# visited = [0 for _ in range(100001)]
# print(bfs(n))


import sys
from collections import deque
input = sys.stdin.readline

def bfs2(v):
    cnt = 0
    que = deque([[v, cnt]]) # 2
    while que:
        v = que.popleft()
        now = v[0]
        cnt = v[1]
        if not visited[now]:
            visited[now] = True
            if now == k:
                return cnt
            cnt += 1
            if 0 <= (now * 2) <= 100000:
                que.append([now*2, cnt])
            if 0 <= (now + 1) <= 100000:
                que.append([now+1, cnt])
            if 0 <= (now - 1) <= 100000:
                que.append([now-1, cnt])
    return cnt

n, k = map(int, input().split())
visited = [False]*100001
print(bfs2(n))