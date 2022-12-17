# 백준 15486 퇴사 2

import sys
input = sys.stdin.readline

n = int(sys.stdin.readline().rstrip())
lst1 = []
lst2 = []
for _ in range(n):
    t, p = map(int, sys.stdin.readline().rstrip().split())
    lst1.append(t)
    lst2.append(p)
dp = [0 for _ in range(n+1)]
ans = dp[0]
for i in range(n):
    ans = max(ans, dp[i])
    # i번까지 얻을 수 있는 dp 중 최댓값 ans
    rst = lst1[i] + i
    # i번 상담을 할 경우 rst날까지 상담해야 한다.
    if rst > n:
        continue
    # 상담 자체를 하지 못하는 경우
    dp[rst] = max(ans + lst2[i], dp[rst])
    # rst 날까지 i번 상담을 한다면 p[i]를 더한 값으로 갱신
    # 상담을 하지 않는 이득이 더 크다면 그대로.
print(max(dp))