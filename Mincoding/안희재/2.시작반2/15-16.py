arr = [[''] * 3 for _ in range(3)]
word = input()

tmp = ord(word)
i = 0
while i < 3:
    j = 0
    while j < i+1:
        arr[2-i][j] = chr(tmp)
        tmp += 1
        j += 1
    i += 1

for i in range(3):
    print(*arr[i],sep='')