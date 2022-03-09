arr1 = []*5
arr2 = []*5

str = input()

for i in range(ord(str), ord(str)+5, 1):
    arr1.append(chr(i))

for i in range(ord(str), ord(str)-5, -1):
    arr2.append(chr(i))
    
for i in range(len(arr1)):
    print(arr1[i], end='')
print()
for i in range(len(arr1)):
    print(arr2[i], end='')
    