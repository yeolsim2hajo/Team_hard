arr = [['a','b','E'],['E','2','W'],['3', '2', '4']]

for i in range(3):
    for k in range(3):
        if ord('A') <= ord(arr[i][k]) <= ord('Z'):
            arr[i][k] = arr[i][k].lower()
        elif ord('a') <= ord(arr[i][k]) <= ord('z'):
            arr[i][k] = arr[i][k].upper()
        else:
            arr[i][k] = int(arr[i][k])
            arr[i][k] += 5


for i in range(3):
    for k in range(3):
        print(arr[i][k], end= ' ')
    print()
