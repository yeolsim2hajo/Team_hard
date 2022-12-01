# 백준 18353 병사 배치하기

import sys
input = sys.stdin.readline

n = int(input())
data = [0]
ans = [0]*(2+n)
for i in range(1, n+1):
    t, p = map(int, input().split())
    data.append((i, t, p))
for i in range(1, n+1):
    day, t, p = data[i]
    if day + t <= n+1:
        ans[i] += p
        for j in range(day+t, n+1):
            ans[j] = max(ans[day], ans[j])
print(max(ans))