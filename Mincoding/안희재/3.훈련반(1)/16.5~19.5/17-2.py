arr = [5,9,4,6,1,5,8,9]

index, target = map(int,input().split())

arr1 = arr[index:]

for i in range(len(arr1)):
    if target == arr1[i]:
        print(i)
