# 상담을 해서 얻을 수 있는 최대 이익
# 상담은 순서대로 진행되며, 1일에 3일이 걸리는 상담을 하면 -> 2,3일 상담은 불가
# N=7인 경우, 5일에 2일이 걸리는 상담을 하게되면, 6,7일은 불가 (N+1인 8일은 퇴사)
    # 마지막 날의 경우, 상담소요시간이 1이 아닌경우는 모두 할 수 없음

# dp임에도 오히려 시간은 2500ms..
# https://dndi117.tistory.com/entry/aaa
import sys 
input = sys.stdin.readline

n = int(input())
t,p = [],[]
# bucket처럼, 해당 정보(소요시간, 보상)들을 쭉 넣어주기
for i in range(n):
    x,y = map(int,input().split())
    t.append(x)
    p.append(y)

dp = [0] * (n+1)
M = 0 
for i in range(n):
    M = max(M,dp[i]) # M을 계속 갱신
    if i+t[i] > n: # 최종기한을 넘기게 되면 고려x
        continue 

    # 해당 일수를 시작하냐 or 시작하지 않느냐가 point
    # 해당 일수를 시작해서 max값이 갱신된다면, dp에 담아주기
    # 갱신되지 않는다면, 이전의 max값이 담겨있는 상태
    # 해당 예시에서: dp = [0,0,0,10,30,0,45, 0] -> max(dp) = 45
                    #     1 2 3  4  5 6  7
    dp[i+t[i]] = max(M+p[i],dp[i+t[i]])
print(max(dp))