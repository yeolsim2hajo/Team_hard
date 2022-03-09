arr = [[4,5,7,1,3,2], ['D','F','Q','W','G','Z']]
num = int(input())

target = 0
for i in range(6):
    if arr[0][i] == num:
        target = i
    
print(arr[1][target])