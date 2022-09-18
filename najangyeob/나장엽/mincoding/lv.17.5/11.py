arr = [3,5,4,2]
mask = list(map(int, input().split()))


masked_arr = [0]*4

for i in range(4):
    if mask[i] == 1:
        masked_arr[i] = arr[i]


result = 0
for k in range(len(masked_arr)):
    result += masked_arr[k]

print(result)