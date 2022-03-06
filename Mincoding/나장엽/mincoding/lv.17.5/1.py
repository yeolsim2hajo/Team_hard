arr = [3,4,1,1,2,6,8,7,8,9,10]
index = int(input())
def getSum(index, arr):
    sum = 0
    for idx in range(index, index+5, 1):
        sum = sum+arr[idx]
    return sum

print(getSum(index, arr))