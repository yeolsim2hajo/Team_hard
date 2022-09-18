from re import L


arr = ['S','t','r','u','c','t','P','o','i','n','t','e','r']
str = input()
flag = 0
for i in range(len(arr)):
    if arr[i] == str:
        flag = 1
        
if flag :
    print('발견')
else:
    print('미발견')