computer = int(input()) # 컴퓨터의 대수
connection = int(input()) # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
network = [[]*computer for _ in range(computer+1)] # 계산 편의를 위해 +1 증가시켜서 초기화

for i in range(connection):
    n1, n2 = map(int, input().split())
    network[n1].append(n2)
    network[n2].append(n1)
   
# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

cnt = 0
visited = [0]*(computer+1) # for 계산편의
def dfs(node):
    global cnt
    visited[node] = 1 # 방문처리
    for i in network[node]:
        if visited[i] == 0: # 방문하지 않았다면? dfs로 다시 들어가기
            dfs(i) 
            cnt += 1 

    
dfs(1) # 1번 컴퓨터와 연결된 컴퓨터를 찾기 위해 1번 노드부터 시작
print(cnt)
# print(visited) #[0, 1, 1, 1, 0, 1, 1, 0] -> 1번 computer과 연결된 computer