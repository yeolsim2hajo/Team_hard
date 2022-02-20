arr = []
def Input(arr):
    arr = list(map(int,input().split()))
    return arr

def output(arr):
    for i in Input(arr)[::-1]:
        print(i, end = '')

output(arr)
