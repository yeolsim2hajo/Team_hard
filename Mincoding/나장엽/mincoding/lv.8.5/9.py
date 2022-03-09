arr = [[0]*3 for _ in range(6)]

a, b = map(int, input().split())

for i in range(0,3):
    for k in range(3):
        arr[i][k] = a
        
for i in range(3,6):
    for k in range(3):
        arr[i][k] = b
        
for i in range(len(arr)):
    for k in range(3):
        print(arr[i][k], end='')
    print()