arr = [[''] * 5 for _ in range(4)]

ca, cb = 0, 0
for i in range(4):
    word = input()
    for j in range(len(word)):
        arr[i][j] = word[j]
        if word[j] == 'A':
            ca = 1
        if word[j] == 'B':
            cb = 1

if ca+cb == 2:
    print('대발견')
elif ca+cb == 1:
    print('중발견')
else:
    print('미발견')
