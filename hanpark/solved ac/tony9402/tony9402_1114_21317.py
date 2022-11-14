# 백준 21317 징검다리 건너기

import sys
input = sys.stdin.readline

n = int(input())
lst = [[list(map(int, input().strip().split()))] for _ in range(n-1)]
k = int(input())
if n==1:
    print(0)
    exit()
elif n==2:
    print(lst[0][0])
    exit()
dp=[0]*n
dp[1]=lst[0][0]
dp[2]=min(lst[0][0]+lst[1][0], lst[0][1])
for i in range(3, n):
    dp[i]=min(lst[i-1][0]+dp[i-1], lst[i-2][1]+dp[i-2])
res=dp[-1]
dp2=dp[:]
for i in range(0, n-3):
    if dp[i]+k<dp[i+3]:
        dp2[i+3]=dp[i]+k
        for j in range(i+4, n):
            dp2[j]=min(dp[j], dp2[j-1]+lst[j-1][0], dp2[j-2]+lst[j-2][1])
        if dp2[-1]<res:
            res=dp2[-1]
print(res)