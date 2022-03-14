a, b = input().split()

arr = ['D','F','G','D','A','Q']

flag = 0
for i in range(len(arr)):
    if ord(a) <= ord(arr[i]) <= ord(b):
        flag = 1

if flag :
    print('발견!!!')
else:
    print('미발견!!!')