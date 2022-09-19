# 2108 통계학
# from statistics import multimode
# N = int(input())
# numbers = []
# total = 0
# for _ in range(N):
#     numbers.append(int(input()))
#     total += numbers[-1]
# numbers.sort()
# mode = multimode(numbers)
# if len(mode) >= 2:
#     freq = mode[1]
# else:
#     freq = mode[0]
# print(total//N, numbers[N//2],
#       freq, numbers[-1]-numbers[0], sep='\n')


#2164 카드2
from collections import deque
N = int(input())
if N == 1:
    print(1)
else:
    cards = deque(range(1,N+1))
    while True:
        cards.popleft()
        if len(cards) == 1:
            break
        card = cards.popleft()
        cards.append(card)
        if len(cards) == 1:
            break
    print(cards[0])

#2164 카드2
from collections import deque
N = int(input())
if N == 1:
    print(1)
else:
    cards = deque(range(2,N+1,2))
    if len(cards) > 1:
        if N%2:
            card = cards.popleft()
            cards.append(card)
        while True:
            cards.popleft()
            if len(cards) == 1:
                break
            card = cards.popleft()
            cards.append(card)
            if len(cards) == 1:
                break
    print(cards[0])
