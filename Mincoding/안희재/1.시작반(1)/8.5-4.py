arr = [''] * 17
word = input().split()

for i in range(17):
    if i < 7:
        arr[i] = word[0]
    elif i < 13:
        arr[i] = word[1]
    else:
        arr[i] = word[2]

print(*arr[::-1],sep='')