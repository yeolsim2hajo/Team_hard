arr = [[0]*5 for _ in range(3)]
str = input()
str = ord(str)
for i in range(3):
    for k in range(5):
        arr[i][k] = chr(str)
        str += 1

print(arr[2][2].lower())