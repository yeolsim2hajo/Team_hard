#221211
N = int(input())
seed = 0
for i in range(N, 0, -1):
    seed += N/i
print(seed)