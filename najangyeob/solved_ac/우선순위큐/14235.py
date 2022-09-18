# 세계 곳곳에 거점을 세워 그 곳을 방문하며 선물을 충전,
# 착한 아이들을 만날 때마다 가장 가치가 큰 선물을 하나 선물
# 방문한 아이들과 거점지의 정보가 주어졌을 때, 아이들이 준 선물들의 가치를 출력
# 아이들에게 줄 선물이 없다면 -1 출력

# n : 아이들과 거점지를 방문한 횟수 n
# 
import sys
input = sys.stdin.readline

n = int(input())
present = []
for _ in range(n):
    a = list(map(int, input().split()))
    if a[0] == 0: # 아이들을 만났는데, 
        if len(present) == 0: # 선물이 없다면
            print(-1) # -1 출력
        else:
            max_idx = present.index(max(present))
            print(present.pop(max_idx))
        
    else:
        for i in range(a[0]):
            present.append(a[i+1])







