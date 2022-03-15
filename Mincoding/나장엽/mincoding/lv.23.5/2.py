arr = [[0]*4 for _ in range(3)]

for i in range(3):
    y, x = map(int, input().split())
    arr[y][x] = '#'
result1 = []
for i in range(3):
    cnt = 0
    for k in range(4):
        if arr[i][k] == '#':
            cnt += 1
        result1.append(cnt)
result2 = []
for k in range(4):
    cnt = 0
    for i in range(3):
        if arr[i][k] == '#':
            cnt += 1
        result2.append(cnt)

flag1 = 0
for i in result1:
    if i >= 2:
        flag1 = 1
flag2 = 0
for i in result2:
    if i >= 2:
        flag2 = 1

if flag1 or flag2 == 1:
    print('위험')
else:
    print('안전')
