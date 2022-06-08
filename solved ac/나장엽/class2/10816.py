
from collections import Counter
import sys
input = sys.stdin.readline

# 시간초과, 이진탐색 시간초과
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

# for target in targets:
#     cnt = 0
#     for card in cards:
#         if target == card:
#             cnt += 1
    
#     print(cnt, end = ' ')


dict = {}

for card in cards:
    if card in dict:
        dict[card] += 1

    else:
        dict[card] = 1

for target in targets:
    if target in dict:
        print(dict[target], end = ' ')
    else:
        print(0, end = ' ')