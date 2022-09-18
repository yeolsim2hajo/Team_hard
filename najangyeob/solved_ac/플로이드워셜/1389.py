# 최대 6단계 이내에서 서로 아는 사람으로 연결될 수 있다고 한다.
# 케빈 베이컨 게임은 임의의 두 사람이 최소 몇 단계 만에 이어질 수 있는지 계산하는 게임

# 미국 헐이우드 배우들끼리 게임을 했을 때 나오는 단계의 총 합이 가장 적은 사람 - > 케빈 베이컨
# 케빈 베이건의 최소값을 찾으려고 한다.
# 1 3
# 1 4
# 2 3
# 3 4
# 4 5


from collections import defaultdict
import heapq

user, relation  = map(int, input().split())
graph = defaultdict(list)

for _ in range(relation):
    p, r = map(int, input().split())
    graph[p].append((r, 1))
    graph[r].append((p, 1))

answer = []
print(graph)
for k in range(1, user+1): # k는 사람
    que = [(0, k)] # cnt, person
    distance = defaultdict(int)
    while que:
        cnt, node = heapq.heappop(que)
        if node not in distance:
            distance[node] = cnt # 몇 단계를 거쳐 아는 사람인지!!
            for p, r in graph[node]: 
                heapq.heappush(que, (cnt+r, p)) # 연결된 노드들 간의 거리를 1로 설정했기에... !!!
    answer.append((sum(distance.values()), k)) # 전체 몇 단계인지 다 더해서 answer에 노드 번호와 총 단계합을 append
answer.sort()
print(answer)
print(answer[0][1])



# 플로이드 워셜
# 모든 사람들에 대해서 계산을 해야하므로...!
# 
# INF = int(1e9)

# N, M = map(int, input().split())

# relation = [[INF] * N for _ in range(N)]

# for i in range(N):
#     relation[i][i] = 0

# for _ in range(M):
#     start, end = map(int, input().split())
#     relation[start-1][end-1] = 1
#     relation[end-1][start-1] = 1

# 모든 경우를 체크하면서 최솟값을 업데이트 하는 알고리즘
# for k in range(N):
#     for a in range(N):
#         for b in range(N):
#             relation[a][b] = min(relation[a][b], relation[a][k]+relation[k][b])

# answer = INF
# index = INF
# for i in range(len(relation)):
#     if sum(relation[i]) < answer:
#         answer = sum(relation[i])
#         index = i
# print(index+1)