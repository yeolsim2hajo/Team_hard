from re import L


arr = [
    [3,4,1,5],
    [3,4,1,3],
    [5,2,3,6]
]

def col_sum(arr):
    result = []
    for i in range(4):
        sum = 0
        for k in range(3):
            sum += arr[k][i]
        result.append(sum)
    return result


sum = col_sum(arr)

index = int(input())

print(sum[index])