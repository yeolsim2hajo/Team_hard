arr = ['A','1','1','1','5','A','w','z']

word = input()

cnt = 0
for i in arr:
    if i == word:
        cnt += 1

if cnt >= 3:
    print('THREE')
elif cnt == 2:
    print('TWO')
elif cnt == 1:
    print('ONE')
else:
    print('NOTHING')