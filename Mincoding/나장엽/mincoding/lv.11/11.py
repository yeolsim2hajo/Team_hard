arr = [[1,3,6,2],[4,2,4,5],[6,3,7,3],[1,5,4,6]]

n = int(input())
select = []

for i in range(4):
    for k in range(4):
        if arr[i][k] > n:
            select.append(arr[i][k])

print(*select, sep=' ')