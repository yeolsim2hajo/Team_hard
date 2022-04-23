arr = ['BBQWORLD', 'KFCAPPLE', 'LOT']
word = input()

cnt = 0
for i in range(3):
    for j in range(len(arr[i])):
        if arr[i][j] == word:
            cnt += 1

print(cnt)