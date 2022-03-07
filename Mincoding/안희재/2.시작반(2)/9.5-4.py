arr = [[10,3,20], [60,30,40], [20,30,40]]
a, b = map(int,input().split())

cnt = 0
for i in range(3):
    for j in range(3):
        if a <= arr[i][j] <= b:
            cnt +=1 

print(cnt)