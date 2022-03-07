arr = [[3,4,1,5], [3,4,1,3,], [5,2,3,6]]

sum = []
for i in range(4):
    result = 0
    for j in range(3):
        result += arr[j][i]
    sum.append(result)

n = int(input())

print(sum[n])