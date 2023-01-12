#221021
from heapq import heappush, heappop
N, M, K = map(int, input().split())
info = []
total = 0
for _ in range(1, K+1):
    pref, level = map(int, input().split())
    heappush(info, (level, -pref))

min_level = 2**31
total = 0
for _ in range(N):
    element = heappop(info)
    total -= element[1]
    min_level = min(min_level, element[0])
    heappush(info, element)

if total < M:
    print(-1)
else:
    q = [(0,0)]
    min_level = 2**31 * N
    while info:
        now_level, now_hate = heappop(info)
        length = len(q)
        for i in range(length):
            total_hate, total_level = q[i]
            new_hate, new_level = total_hate+now_hate, total_level+now_level
            q.append((new_hate, new_level))
            if new_hate <= -M:
                pass



# 조합

# M이 선호도 합보다 크면 -1
# 간 레벨 최소, 도수 최대
