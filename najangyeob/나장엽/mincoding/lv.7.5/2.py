arr = [0]*6
index = list(map(int, input().split()))


for i in range(len(index)):
    arr[index[i]] = 1

for i in range(len(arr)):
    print(arr[i], end= ' ')