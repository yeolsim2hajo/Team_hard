arr = [8,3,12,10,1]
arr_len=int(len(arr))


for i in range(arr_len -1, 0, -1): # 4 3 2 1
    for j in range(i): # i가 4일때 j는 0 1 2 3 i가 3일때 j는 0 1 2 
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]


            