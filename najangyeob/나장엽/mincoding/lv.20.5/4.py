arr1 = [ list(map(int, input().split())) for _ in range(4)]
arr2 = [ list(map(int, input().split())) for _ in range(4)]



dat = [[0,0,0,0] for _ in range(4)]



for i in range(4):
    for k in range(4):
        dat[i][k] = arr1[i][k] + arr2[i][k]

result = 0
for j in range(4):
    for l in range(4):
        if dat[j][l] == 2:
            result = 1

if result == 1:
    print('걸리다')
else:
    print('걸리지않는다')