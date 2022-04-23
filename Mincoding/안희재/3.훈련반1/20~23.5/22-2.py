arr = [input() for _ in range(3)]

if arr[0] == arr[1] and arr[1] == arr[2]:
    print('WOW')
elif arr[0] != arr[1] and arr[0] != arr[2] and arr[1] != arr[2]:
    print('BAD')
else:
    print('GOOD')