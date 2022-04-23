arr = [[' '] * 4 for _ in range(3)]
num = int(input())
tmp = num
# (0,2)(0,3)
# (1,1)(1,2)(1,3)
# (2,0)(2,1)(2,2)(2,3)
for i in range(3): # 2,3,4갯수
    for j in range(i+1,-1,-1):
        arr[i][3-j] = tmp
        tmp += 1

for i in range(3):
    print(*arr[i],sep='')