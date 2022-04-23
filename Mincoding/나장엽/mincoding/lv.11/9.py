arr = list(input().split())

big = []
small = []

for i in range(len(arr)):
    if ord('A') <= ord(arr[i]) <= ord('Z'):
        big.append(arr[i])
    else:
        small.append(arr[i])
        
print('big=', end='')
print(*big, sep='')
print('small=', end='')
print(*small, sep='')