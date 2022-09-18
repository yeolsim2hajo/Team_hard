arr = ['A','1','1','1','5','A','w','z']

str = input()


cnt = 0
for i in range(len(arr)):
    if arr[i] == str:
        cnt += 1

if cnt >= 3:
    print('THREE')
elif cnt >= 2:
    print('TWO')
elif cnt >= 1:
    print('ONE')
else:
    print("NOTHING")
