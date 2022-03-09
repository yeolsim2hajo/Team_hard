arr = [0]*5

n = int(input())

for k in range(len(arr)):
    arr[k] = n
    n -= 1

def KFC():
    for i in range(len(arr)):
        print(arr[i], end='')
KFC()