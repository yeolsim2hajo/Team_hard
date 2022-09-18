arr = [[0]*3 for _ in range(2)]

def fn(arr):
    num = list(map(int, input().split()))
    temp = 0
    for i in range(2):
        for k in range(3):
            arr[i][k] = num[temp]
            temp += 1
    return arr

def process(arr):
    sum = 0
    for i in range(2):
        for k in range(3):
            sum += arr[i][k]
    return sum

def output(n):
    print(n)
    
fn(arr)
output(process(arr))