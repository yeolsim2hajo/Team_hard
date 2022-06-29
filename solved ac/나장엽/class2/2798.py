# M을 넘지 않으면서 M과 최대한 가깝게 만들기
def dfs(level, Sum):
    if Sum > M:
        return

    if level == 3:
        result.append(Sum)
        return

    for i in range(len(cards)):
        if used[i] == 1: continue
        used[i] = 1
        dfs(level+1, Sum+cards[i])
        used[i] = 0

import sys
input = sys.stdin.readline


N, M = map(int, input().split())
cards = list(map(int, input().split()))
result = []
used = [0]*N

dfs(0, 0)
print(max(set(result)))
# 시간 472ms
    
    
from itertools import combinations
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
card_list = list(map(int, input().split()))
Max = 0
for cards in combinations(card_list, 3):
    temp_sum = sum(cards)
    if Max < temp_sum <= M:
        Max = temp_sum
print(Max)

# 시간 104ms