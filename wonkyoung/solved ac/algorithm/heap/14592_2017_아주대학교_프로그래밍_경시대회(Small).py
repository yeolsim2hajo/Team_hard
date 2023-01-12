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

# heapify
def find_winner():
    from heapq import heapify, heappop
    N = int(input())
    heap = []
    for i in range(N):
        score, submit_cnt, upload_time = map(int, input().split())
        heap.append((-score, submit_cnt, upload_time, i))
    heapify(heap)
    return heappop(heap)[-1]
print(find_winner() + 1)

# 한꺼번에 받기
def find_winner():
    from heapq import heappush, heappop
    N = int(input())
    heap = []
    for i in range(N):
        info = list(map(int, input().split()))
        info[0] = -info[0]
        heappush(heap, (*info, i))
    return heappop(heap)[-1]
print(find_winner() + 1)

# return 값 조절
def find_winner():
    from heapq import heappush, heappop
    N = int(input())
    heap = []
    for i in range(N):
        info = list(map(int, input().split()))
        info[0] = -info[0]
        heappush(heap, (*info, i))
    return heappop(heap)
print(find_winner()[-1] + 1)

