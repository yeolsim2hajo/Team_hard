arr = [[3,5,9], [4,2,1], [1,1,5]]

sum = 0 # 아 또 이거 안에 써서 틀렸네.. 이 실수 이제 고치자..
for i in range(3):
    T = list(map(int,input().split()))
    for j in range(3):
        if T[j]:
            sum += arr[i][j]

print(sum)