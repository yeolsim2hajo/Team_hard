arr = [3,5,4,2]
mask = list(map(int,input().split()))

sum = 0
for i in range(4):
    if mask[i] == 1:
        sum += arr[i]

print(sum)