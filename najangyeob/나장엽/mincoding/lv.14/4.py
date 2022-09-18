arr = list(input().split())

for i in range(5): # 0 
    for k in range(0+i,5,1): # 0 5 / 1 5 / 2 5 / 3 5 / 4 5 
        print(arr[k], end= ' ')
    print()