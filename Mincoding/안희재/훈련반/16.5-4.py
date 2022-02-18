index0, index1 = map(int,input().split())

original_arr = [0] * 6
original_arr[0] = index0
original_arr[1] = index1

for i in range(2,6):
    original_arr[i] = original_arr[i-2] * original_arr[i-1]

print(original_arr[5])