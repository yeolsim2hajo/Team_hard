# 최소 -> bfs! (dfs xx)
# "단, 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다."" -> backtracking
# 처음에, 재방문 방지 코드 안 넣었는데 계속 오류 떴음 ㅠㅠ
    # 코드 더 철저히 짜자;;
    # 아무리 문제에서 안 나와있어도 변명이 못 됨. 개발자는 항상 발전하고 더 나은 것을 찾아야 함ㅇㅇ.
from collections import deque
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split()) # N은 처음 수 / M은 도착 수
    visit = [0] * 1000001 # 재방문 방지용 - 1번인덱스 = 1번에 두기 위해 *1000001
    visit[N] = 1 # 시작값은 미리 체크
    def bfs(N,cnt):
        q = deque()
        q.append((N,cnt)) # 초기값

        while q:
            result, cnt = q.popleft()

            if result == M:
                return cnt
            
            for i in range(4):
                if i == 0:
                    if result+1 > 1000000: continue # 연산 중간 결과는 항상 100만 이하
                    if visit[result+1] == 1: continue # 이미 나온 중간 결과라면, pass
                    visit[result+1] = 1
                    q.append((result+1,cnt+1))
                elif i == 1:
                    if visit[result-1] == 1: continue # 빼는 경우, result-1 > 1000000 할 필요x
                    visit[result-1] = 1
                    q.append((result-1,cnt+1))
                elif i == 2:
                    if result*2 > 1000000: continue
                    if visit[result*2] == 1: continue
                    visit[result*2] = 1
                    q.append((result*2,cnt+1))
                else:
                    if visit[result-10] == 1: continue
                    visit[result-10] = 1
                    q.append((result-10,cnt+1))

                


    print(f'#{tc} {bfs(N,0)}')