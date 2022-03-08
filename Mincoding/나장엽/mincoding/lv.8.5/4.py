arr = list(input().split())


result = ['']*17
for i in range(0, 17, 1):
    if 0<= i <= 6:
        result[i] = arr[0]
    elif 6 < i < 13:
        result[i] = arr[1]
    else:
        result[i] = arr[2]

for i in range(len(result)-1, -1, -1):
    print(result[i], end='')