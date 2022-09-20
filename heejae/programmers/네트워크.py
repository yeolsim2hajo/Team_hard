# 프로그래머스 제출용 코드
def solution(n, computers):
    answer = 0
    group = [0] * n

    for i in range(n):
        computers[i][i] = 0 # ㅎ;ㅎ;

    def dfs(start):
        if sum(computers[start]) == 0:
            return # 더이상 가지 뻗어나갈게 없다는 뜻

        for i in range(n):
            if computers[start][i] > 0: # 1이란 뜻
                computers[start][i], computers[i][start] = 0, 0 # 침몰
                if not i in path: # 이거 쓰면, 깊이탐색해도 ㄱㅊㅋㅋㅋㅋused안써도됨 ㅋㅋ
                    path.append(i)
                dfs(i)

    for i in range(n):
        path = []
        path.append(i) # 처음 시작할 놈이 보스. 일단 0번인덱스에 보스 두고 시작
        dfs(i)
        if len(path) >= 2: # 자기이외에도 그룹원이 있다는 뜻
            for i in range(1,len(path)): # 0번인덱스는 보스니까 ㄱㅊ
                group[path[i]] = 1 # 1이란 뜻은 그룹에 속해있다

    answer = group.count(0)
    return answer