arr1 = [[0,0,0,1], [1,1,0,1], [1,0,0,1], [1,1,1,1]]
arr2 = [[1,1,1,1], [1,0,1,1], [1,0,0,0], [1,0,0,0]]

for i in range(4):
    for j in range(4):
        if arr2[i][j] == 1 and arr1[i][j] == 0:
            arr1[i][j] = 1
# 합치기 완료

for i2 in range(4):
    for j2 in range(4):
        if arr1[i2][j2] == 0:
            print(f'({i2},{j2})')