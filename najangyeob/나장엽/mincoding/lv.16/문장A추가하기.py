arr = [""]*6
str = list(input())
index = int(input())

# str을 arr에 추가
for i in range(0, len(str)):
    arr[i] = str[i]

for idx in range(len(str), index, -1):
    arr[idx] = arr[idx-1]

arr[index] = 'A'


for k in range(0, len(arr)):
    print(arr[k], end='')