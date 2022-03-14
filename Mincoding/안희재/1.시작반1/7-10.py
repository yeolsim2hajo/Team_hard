word = input()

def input():
    arr = [[word] * 4 for _ in range(4)]
    return arr

def output(arr):
    for i in range(4):
        print(*arr[i],sep='')

output(input())