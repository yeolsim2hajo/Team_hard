word = input()
arr = [[0] * 5 for _ in range(3)]

tmp = 0
for i in range(3):
    for j in range(5):
        arr[i][j] = chr(ord(word)+tmp)
        tmp += 1


result = arr[2][2].lower()
print(result)