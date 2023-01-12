from heapq import heappop, heappush
N, M = map(int, input().split())
staff = list(map(int, input().split()))
balloon = []
for minute in staff:
    heappush(balloon, (0, minute))

cnt = pre = real = 0
while cnt < M:
    now, after = heappop(balloon)
    minute = now+after
    real = max(real, pre, minute)
    heappush(balloon, (minute, after))
    cnt += 1
    pre = now

print(real)


