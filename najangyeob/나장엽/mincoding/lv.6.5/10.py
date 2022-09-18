arr = list(input().split())

max = ord(arr[0])
compare = ord(arr[0])

for i in range(len(arr)):
    if max < ord(arr[i]):
        max = ord(arr[i])
        

if compare == max:
    print("옳다{}".format(chr(compare)))
else:
    print("옳지않음")