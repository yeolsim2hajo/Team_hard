arr = ['#', '_', '#', '_', '#', '#']

result = []
for i in range(len(arr)):
    if arr[i] == '#':
        result.append('샵')
    else:
        result.append('무')
        
for i in range(len(result)):
    print(result[i], end='')