# 원경코드를 수정한 코드 -> 성공은했으나, deepcopy써서 그런지, tc1은 여전히 3300ms..
    # deepcopy대신에, pop(인덱스) 넣어서 처리했음
    # 여전히, "통과 (654.31ms, 15.2MB)" => 오래걸리긴 함..ㅠㅠ
    # DFS가 아닌가.....
def dfs(lst,ans,arg=0):
    global answer,visited,length
    if arg == length:
        result.append(answer)
        return

    tmp = []
    for i in range(len(lst)):
        if visited[i] == 0:
            tmp.append(lst[i][0])

    if sum(visited) != 5 and  not(ans in tmp):
        return

    for i in range(length):
        if lst[i][0] == ans and visited[i] == 0:
            visited[i] = 1
            answer.append(lst[i][1])
            tmp2 = len(answer)-1 # 요기
            dfs(lst,lst[i][1],arg+1)
            answer = answer[:tmp2] # 요기
            visited[i] = 0

def solution(tickets):
    global answer,length,visited, result
    result = []
    answer = []
    length = len(tickets)
    visited = [0]*length
    tickets.sort(key=lambda x:x[1])
    answer.append('ICN')
    dfs(tickets,'ICN')

    return result[0]

print(solution([["ICN", "BBB"],["ICN", "CCC"],["BBB", "CCC"],["CCC", "BBB"],["CCC", "ICN"]]))
