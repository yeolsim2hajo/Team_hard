a, b = input().split()

arr = [['']*6 for _ in range(3)]

for i in range(3):
    for k in range(4):
        arr[i][k] = a
for i in range(3):
    for k in range(4, 6):
        arr[i][k] = b
        
for i in range(3):
    for k in range(6):
        print(arr[i][k], end='')
    print()
        