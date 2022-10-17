#221017
from heapq import heappush, heappop
N = int(input())
heap = []
for i in range(N):
    score, submit_cnt, upload_time = map(int, input().split())
    heappush(heap, (-score, submit_cnt, upload_time, i))
winner = heappop(heap)
print(winner[-1] + 1)


# 함수로
def find_winner():
    from heapq import heappush, heappop
    N = int(input())
    heap = []
    for i in range(N):
        score, submit_cnt, upload_time = map(int, input().split())
        heappush(heap, (-score, submit_cnt, upload_time, i))
    return heappop(heap)[-1]
print(find_winner() + 1)


# 정렬
def find_winner():
    N = int(input())
    heap = []
    for i in range(N):
        score, submit_cnt, upload_time = map(int, input().split())
        heap.append((-score, submit_cnt, upload_time, i))
    heap.sort()
    return heap[0][-1]
print(find_winner() + 1)

