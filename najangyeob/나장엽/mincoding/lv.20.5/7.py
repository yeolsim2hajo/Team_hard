arr = list(input())

for i in range(len(arr)):
    str = arr[0:i+1]
    print(''.join(str))