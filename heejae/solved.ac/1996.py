N = int(input())
li = ['.'*(N+2)] + ['.'+input()+'.' for _ in range(N)] + ['.'*(N+2)]
res = []
for i in range(N):
    i += 1
    s = ''
    for j in range(N):
        j += 1
        if ord('0') <= ord(li[i][j]) <= ord('9'):
            s += '*'
        else:
            bomb = 0
            for a in range(i-1, i+2):
                for b in range(j-1, j+2):
                    if ord('0') <= ord(li[a][b]) <= ord('9'):
                        bomb += int(li[a][b])
            s += str(bomb) if bomb < 10 else "M"
    res.append(s)
for s in res:
    print(s)