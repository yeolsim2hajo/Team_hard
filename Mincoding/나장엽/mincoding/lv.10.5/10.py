arr = [ [1,0,0,0,0],
        [1,0,1,0,0],
        [1,1,0,1,0],
        [1,0,1,0,0],
        [0,1,0,0,1],
        [0,0,0,1,0],
        [1,1,0,0,0]]

def Input():
    n = int(input())
    return n

def process(arr, n):
    cnt = 0
    for i in range(7):
        if arr[i][n] == 1:
            cnt += 1
    return cnt
def output(n):
    print(n)

output(process(arr, Input()))
