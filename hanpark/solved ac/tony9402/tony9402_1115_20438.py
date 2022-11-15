# 백준 20438 출석체크

import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())

k_li = list(map(int, input().split()))
q_li = list(map(int, input().split()))

dp = [1] * (n + 3)

while q_li:
    start = q_li.pop(0)

    if start not in k_li:
        for num in range(1, ((n + 2) // start) + 1):
            if start * num not in k_li:
                dp[start * num] = 0


dp_sum = [0] * (n + 3)

for num in range(3, n + 3):
    if num == 3:
        dp_sum[num] = dp[num]

    else:
        dp_sum[num] = dp[num] + dp_sum[num - 1]


for _ in range(m):
    i, j = map(int, input().split())
    print(dp_sum[j] - dp_sum[i - 1])