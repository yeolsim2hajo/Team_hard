#221024
one, two, three = map(int, input().split())
limit = one + two + three
dice_sum = {i:0 for i in range(3, limit+1)}
for i in range(1, one+1):
    for j in range(1, two+1):
        for k in range(1, three+1):
            dice_sum[i+j+k] += 1
freq_key, max_val = 3, 1
for key, value in dice_sum.items():
    if value > max_val:
        max_val = value
        freq_key = key
print(freq_key)

