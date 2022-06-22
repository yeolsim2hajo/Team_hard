# 프로세서 연결하기
T = int(input())
for tc in range(1,1+T):
    N = int(input())
    processor = []
    answer = 0
    for i in range(N):
        processor.append(input().split())
        if i == 0 or i == N-1:
            answer += processor[i].count('1')
        else:
            answer = answer if processor[i][0] == '0' else answer + 1
            answer = answer if processor[i][-1] == '0' else answer + 1
    path = 0
    visited = [[False] * N for _ in range(N)]
    def dfs(arg=answer):
        global path, answer

        for i in range(1,N-1):
            for j in range(1,N+1):
                if visited[i][j] is False and processor[i][j] == '1':
                    dfs(arg+1)

    dfs()

    print(f'#{tc} {answer}')