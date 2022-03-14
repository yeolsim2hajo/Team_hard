arr = [[''] *  6 for _ in range(4)]

for i in range(4):
    word = input()
    for j in range(len(word)):
        arr[i][j] = word[j]

arr2 = []
for i in range(4):
    a = ''.join(arr[i])
    arr2.append(len(a))

arr2.sort()
print(*arr2)