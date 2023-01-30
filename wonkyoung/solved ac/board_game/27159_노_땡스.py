#230130
N = int(input())
cards = list(map(int, input().split()))
total_score = cards[0]
for i in range(1, N):
    if cards[i] != cards[i-1] + 1:
        total_score += cards[i]
print(total_score)