arr = [[1,3,6,2], [4,2,4,5], [6,3,7,3], [1,5,4,6]]

result = []
num = int(input())

for i in range(4):
    for j in range(4):
        if arr[i][j] > num:
            result.append(arr[i][j])

print(*result)
