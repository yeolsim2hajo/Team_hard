arr = [3,5,2,4,1]
arr2 = [[9,8], [7,1], [3,4]]
num = int(input())

if num % 2:
    print(*arr, sep='')
else:
    for i in range(3):
        print(*arr2[i], sep='')