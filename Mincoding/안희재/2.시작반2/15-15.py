arr = [[''] * 8 for _ in range(2)]

for i in range(2):
    word = input()
    for j in range(len(word)):
        arr[i][j] = word[j]

cnt = 0
for i in range(8):
    if arr[0][i] != arr[1][i]:
        cnt += 1

print(cnt)