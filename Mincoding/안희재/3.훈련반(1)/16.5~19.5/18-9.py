arr = [[1,3,3,5,1], [3,6,2,4,2], [1,9,2,6,5]]

bucket = [0] * 10

for i in range(3):
    for j in range(5):
        index = arr[i][j]
        bucket[index] += 1

n = int(input())

for i in range(len(bucket)):
    if bucket[i] == n:
        print(i, end= ' ')