arr = [0]*6

a, b = map(int, input().split())


for i in range(0, 3):
    arr[i] = a
    a += 1
    
for i in range(5, 2, -1):
    arr[i] = b
    b -= 1
    
    
for i in range(len(arr)):
    print(arr[i], end = ' ')