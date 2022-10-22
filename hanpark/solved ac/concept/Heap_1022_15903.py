# 백준 15903 카드 합체 놀이

import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().strip().split())
lst = list(map(int, input().strip().split()))
heapq.heapify(lst)
for _ in range(m):
    x = heapq.heappop(lst)
    y = heapq.heappop(lst)
    heapq.heappush(lst, x+y)
    heapq.heappush(lst, x+y)
print(sum(lst))

# heapify로 변형시켜주기
# 이후 heappop 써서 가장 작은 수들 추출
# 연산을 거친 후 heap에 다시 넣어주기