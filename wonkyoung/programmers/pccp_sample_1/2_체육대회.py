#230226
#2
# 완전 탐색 (dfs) - 시간 많이 나오지만 통과
def solution(ability):
    answer = 0
    N, M = len(ability), len(ability[0])
    visited = [False] * N
    def dfs(level=0, total=0):
        nonlocal answer
        if level == M:
            if answer < total:
                answer = total
            return
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                dfs(level+1, total+ability[i][level])
                visited[i] = False
    dfs()
    return answer