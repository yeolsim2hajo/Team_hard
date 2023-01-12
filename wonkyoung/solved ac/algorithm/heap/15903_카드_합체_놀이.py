#221018
from heapq import heappush, heappop, heapify
N, M = map(int, input().split())
cards = list(map(int, input().split()))
heapify(cards)

for _ in range(M):
    output = []
    for _ in range(2):
        output.append(heappop(cards))

    for _ in range(2):
        heappush(cards, output[0] + output[1])

print(sum(cards))
