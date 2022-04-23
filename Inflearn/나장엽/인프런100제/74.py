graph = {1: [2, 3, 4],
		2: [1, 3, 4, 5, 6],
		3: [1, 2, 7],
		4: [1, 2, 5, 6],
		5: [2, 4, 6, 7],
		6: [2, 4, 5, 7],
		7: [3, 5, 6]}
# 입력
# 1 7
#
# 출력
# 6

# 최장거리...? 마지막 방문을 end?로 처리? 중복없이 한 정점에서 다른 정점까지 경우하는 가장 많은 간선의 수
# 무슨 말인지 모르겠군...???
start, end = map(int, input().split())
que = []
visited = []
que.append(start)
def func(que, visited):
    global end


    if que[-1] == end:
        return len(visited)

    if que[-1] in visited:
        return len(visited)

    visited.append(que[-1])
    answer = 0

    for next in graph[que[-1]]:
        que.append(next)
        answer = max(answer, func(que, visited))
        que.pop(-1)
    return answer

print(func(que, visited))