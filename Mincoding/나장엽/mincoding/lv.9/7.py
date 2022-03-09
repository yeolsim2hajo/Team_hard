arr = [['']*2 for _ in range(6)]

for i in range(6):
        arr[i] = input().split()
cnt = 0
for i in range(6):
    if arr[i][0] < arr[i][1]:
        arr[i][0], arr[i][1] = arr[i][1], arr[i][0]
        cnt+= 1


for i in range(6):
    for k in range(2):
        print(arr[i][k], end= ' ')
    print()
print(f'{cnt}명')