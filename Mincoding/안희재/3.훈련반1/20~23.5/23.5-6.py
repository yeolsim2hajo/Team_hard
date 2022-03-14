base = [['A','B','C','D'], ['B','B','A','B'], ['C','B','A','C'], ['B','A','A','A']]
arr = [[0] * 4 for _ in range(4)]
for i in range(4):
    word = input()
    for j in range(4):
        arr[i][j] = word[j]

ca, cb, cc, cd = 0, 0, 0, 0

for i in range(4):
    for j in range(4):
        if arr[i][j] == base[i][j]:
            if arr[i][j] == 'A':
                ca += 1
            elif arr[i][j] == 'B':
                cb += 1
            elif arr[i][j] == 'C':
                cc += 1
            else:
                cd += 1

if max(ca,cb,cc,cd) == ca:
    print('A')
elif max(ca,cb,cc,cd) == cb:
    print('B')
elif max(ca,cb,cc,cd) == cc:
    print('C')
else:
    print('D')
