#221014
N, K = map(int, input().split())
share_cards = sorted(map(int, input().split()))
my_cards = sorted(map(int, input().split()))

max_val = -1e8
for _ in range(K):
    front = share_cards[0] * my_cards[0]
    back = share_cards[-1] * my_cards[-1]
    if front > back:
        my_cards.pop(0)
    elif front < back:
        my_cards.pop()
    else:
        for i in range(1, N//2+1):
            front = share_cards[i] * my_cards[0]
            back = share_cards[-i-1] * my_cards[-1]
            if front > back:
                my_cards.pop(0)
                break
            elif front < back:
                my_cards.pop()
                break
print(max(share_cards[0] * my_cards[0], share_cards[-1]*my_cards[-1]))






