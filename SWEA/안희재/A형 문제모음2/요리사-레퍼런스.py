# 문교수님 풀이 - 매우 깔끔;; 캬;; 진짜 dfs안에서 해결을 다 해버렸네;
    # 난 구질구질하게 했는데
    # 특히, 다음 dfs를 보낼때, 2개를 써서 각각 보내준 스킬 꼭 보자
import sys
sys.stdin = open('cook_input.txt','r')

def dfs(n,alst,blst):
    global ans
    if n==N:
        if len(alst)==len(blst):
            asum, bsum = 0, 0
            for i in range(len(alst)):
                for j in range(len(alst)):
                    asum += arr[alst[i]][alst[j]]
                    bsum += arr[blst[i]][blst[j]]
            if ans > abs(asum-bsum):
                ans = abs(asum-bsum)
        return

    dfs(n+1,alst+[n],blst)
    dfs(n+1,alst,blst+[n])

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 2e18
    dfs(0,[],[])
    print(f'#{tc}', ans)