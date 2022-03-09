arr = [3,4,1,1,2,6,8,7,8,9,10]
index = int(input())

def getSum(num):
    new_arr = []
    new_arr = arr[num:num+5]
    sum = 0
    for i in new_arr:
        sum += i
    return sum

print(getSum(index))