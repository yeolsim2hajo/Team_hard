arr = ['A','F','G','A','B','C']

a, b = input().split()

flag1 = 0
flag2 = 0
for i in range(len(arr)):
    if arr[i] == a:
        flag1 = 1   
    if arr[i] == b:
        flag2 = 1
        
if flag1 and flag2 == 1:
    print("와2개")
elif flag1 or flag2 == 1:
    print("오1개")
else:
    print("우0개")