arr = []

def input1(arr):
    arr.append(input().split())
    
def output(arr):
        for i in range(-1, -5, -1):
            print(arr[0][i], end='')
        
input1(arr)
output(arr)