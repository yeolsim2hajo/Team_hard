arr = [[0]*4 for _ in range(3)]

def fn(arr):
    n = int(input())
    for i in range(3):
        for k in range(4):
            arr[i][k] = n
            n += 1
    return arr

def process(arr):
    for i in range(3):
        for k in range(4):
            arr[i][k] += 1
    return arr

def output(arr):
    for i in range(3):
        for k in range(4):
            print(arr[i][k], end= ' ')
        print()
        
fn(arr)
process(arr)
output(arr)