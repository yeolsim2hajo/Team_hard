arr1 = [3,5,2,4,1]

arr2 = [[9,8],[7,1],[3,4]]

n = int(input())

if n % 2 == 1:
    for i in range(len(arr1)):
        print(arr1[i], end='')
else:
    for i in range(len(arr2)):
        for k in range(2):
            print(arr2[i][k], end='')
        print()