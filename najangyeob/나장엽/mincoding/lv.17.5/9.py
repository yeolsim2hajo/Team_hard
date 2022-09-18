arr = list(map(int, input().split()))

mask = [1,0,1,0,1,0]

masked_arr = [0]*len(arr)

for idx in range(0, len(mask)):
    if mask[idx] == 1:
        masked_arr[idx] = arr[idx]
        
min = masked_arr[0]

for i in range(0, len(masked_arr), 2):
    if min > masked_arr[i]:
        min = masked_arr[i]
    else:
        min = min

for j in range(len(masked_arr)):
    if masked_arr[j] == min:
        print("arr[{0}]={1}".format(j, min))