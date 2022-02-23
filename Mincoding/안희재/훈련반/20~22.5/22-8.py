arr = [ [[2,4,],[1,5]], [[2,3],[3,6]], [[7,3],[1,5]] ]

n = int(input())

min = 2e18
max = 0
for i in range(2):
    for j in range(2):
        if arr[n][i][j] < min:
            min = arr[n][i][j]
        if arr[n][i][j] > max:
            max = arr[n][i][j]

print(f'MAX={max}')
print(f'MIN={min}')