T = int(input())
def find_winner():
    global winner
    for i in range(6):
        even[cards[2 * i]] += 1
        odd[cards[2 * i + 1]] += 1
        if i >= 2:
            one_cnt = two_cnt = 0
            for j in range(10):
                if even[j]:
                    if even[j] >= 3:
                        winner = 1
                        return
                    elif one_cnt == 0:
                        one_cnt = 1
                    elif even[j - 1]:
                        one_cnt += 1
                        if one_cnt == 3:
                            winner = 1
                            return
                    else:
                        one_cnt = 0
                if odd[j]:
                    if odd[j] >= 3:
                        winner = 2
                        return
                    elif two_cnt == 0:
                        two_cnt = 1
                    elif odd[j - 1]:
                        two_cnt += 1
                        if two_cnt == 3:
                            winner = 2
                            return
                    else:
                        two_cnt = 0
for tc in range(1,1+T):
    cards = list(map(int,input().split()))
    even = [0] * 10
    odd = [0] * 10
    winner = 0
    find_winner()
    print(f'#{tc} {winner}')