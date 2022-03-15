arr = [3,5,1,9,7]

for i in range(4):
    d = input()
    if d == "R":
        temp1 = arr[4]
        for k in range(4, 0, -1):
            arr[k] = arr[k-1]
        arr[0] = temp1

    if d == "L":
        temp2 = arr[0]
        for k in range(4):
            arr[k] = arr[k+1]
        arr[4] = temp2    
            

print(*arr, sep= ' ')