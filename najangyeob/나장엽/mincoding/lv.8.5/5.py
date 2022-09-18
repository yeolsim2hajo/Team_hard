arr = list(input().split())
result = []
for i in range(ord(arr[0]), ord(arr[1])+1, 1):
    result.append(chr(i))
    
for i in range(int(arr[2])):
    print(''.join(result))
    