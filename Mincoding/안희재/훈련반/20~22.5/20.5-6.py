arr = list(map(int,input().split()))

# 3 5 7 1 4 2 8
arr1 = arr[0:3] # 3 5 7
for i in range(4): # 0, 1, 2 ,3
    for j in range(1): # 3, 4,5,6이 각각 더해져야해
        arr1 += [arr[i+3]]
    print(' '.join(map(str,arr1)))

