# dfs 풀이법은 시간초과 날것 같아서 bfs로 풀이
from collections import deque

def solution(info, edges):
    answer = 0
    check = {0: 1, 1: -1} # 양이면 +1, 늑대면 -1
    queue = deque() # queue: (현재 노드, 양의수-늑대수)
    
    queue.append([[0], 1]) # 초기값: 루트 노드는 항상 양이므로 '0', 그리고 양은 +1이므로 '1'
    graph = [[] for _ in range(17)] # 17칸(info의 최대길이는 17)
    
    for i in edges: # edges모두 순회
        graph[i[0]].append([i[1], check[info[i[1]]]])
        
    while queue:
        now, total = queue.popleft()
        cnt = 0
        
        for i in now:
            if info[i] == 0:
                cnt += 1 # 양이면 +1 
                
        answer = max(cnt, answer) # 각 경우의 수마다, cnt와 answer비교해서 최대값 찾기
        
        for i in now:
            for j in graph[i]:
                if j[0] not in now: # 아직 방문 안한 노드라면,
                    if total + j[1] > 0: # 그리고 여태 만난 양+늑대 value가 양수면,
                        queue.append([now + [j[0]], total + j[1]]) # 다음 노드 탐색

    return answer