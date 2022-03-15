arr = [list(input()) for _ in range(4)]



flag1 = 0
flag2 = 0
for i in range(len(arr)): 
    for k in range(len(arr[i])):
        if arr[i][k] == 'A' :
            flag1= 1
        if arr[i][k] == 'B' :
            flag2 = 1

if flag1 and flag2 == 1:
    print('대발견')
elif flag1 or flag2 == 1:
    print('중발견')
else:
    print('미발견')