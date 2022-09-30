# 방 바닥의 세로 크기 n, 가로 크기 m
n,m = map(int, input().split())
graph = [] 	# 2차원 리스트의 맵 정보 저장할 공간
for _ in range(n):
    graph.append(list(input()))
 
# '-'모양의 나무 판자 개수 계산
count = 0
for i in range(n):
    a = ''
    for j in range(m):
        if graph[i][j] == '-':
            if graph[i][j] != a:
                count += 1
        a = graph[i][j]
 
# 'ㅣ'모양의 나무 판자 개수 계산
for j in range(m):
    a = ''
    for i in range(n):
        if graph[i][j] == '|':
            if graph[i][j] != a:
                count += 1
        a = graph[i][j]
 
print(count)