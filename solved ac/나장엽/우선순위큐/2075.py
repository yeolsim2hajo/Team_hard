

# 메모리초과
# max-heap을 이용하여 큐를 n-1번 pop해서 n번째 큰수를 구하기

# import sys
# input = sys.stdin.readline
# import heapq


# N = int(input())
# data = []
# for i in range(N) :
#     table = list(map(int, input().split()))
#     for k in range(N):
#         heapq.heappush(data, -table[k])


# for i in range(N): # 0, 1, 2, 3, 4
#     if i == N - 1:
#         print(-heapq.heappop(data))
#     heapq.heappop(data)



# min-heap 이용
# n번째 큰 숫자를 원하기 때문에 큐의 길이를 n만큼 유지하는 것이 중요하다

import sys
input = sys.stdin.readline
import heapq

N = int(input())
que = []

for _ in range(N):
    numbers = list(map(int, input().split()))
    # 큐의 길이를 n만큼 유지 -> 최소힙의 특징 가장 작은 값이 가장 최상단 노드이다 -> que[0] -> 길이를 n만큼 유지하면 첫번째 값이 바로 n번째 큰 값
    if not que:
        for number in numbers:
            heapq.heappush(que, number)
    else:
        for number in numbers:
            if que[0] < number: # que의 최소값이 number보다 작으면 
                heapq.heappush(que, number) 
                heapq.heappop(que) # 최소값은 삭제

print(que[0])