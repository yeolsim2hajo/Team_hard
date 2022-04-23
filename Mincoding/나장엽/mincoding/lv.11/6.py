arr = [3,4,1,3,2,7,3]

n = int(input())
flag = 0
for i in range(len(arr)):
    if arr[i] == n:
        flag = 1
        
if flag :
    print('발견')
else:
    print('미발견')