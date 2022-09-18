arr1 = [ [0, 0, 0, 1], [1, 1, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1] ]
arr2 = [ [1, 1, 1, 1], [1, 0, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0] ]

result= []

for row in range(4):
    temp=[]
    for col in range(4):
        temp.append(arr1[row][col] + arr2[row][col])
    result.append(temp)


for i in range(4):
    for j in range(4):
        if result[i][j] == 0:
            print("({0},{1})".format(i, j))