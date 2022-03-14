arr = [['a','b','a','c','z'],['c','t','a','c','d'],['c','c','c','c','a']]

str = input()
cnt = 0
for i in range(3):
    for k in range(5):
        if arr[i][k] == str:
            cnt += 1

if cnt >= 7:
    print('세상에')
elif cnt >=5:
    print('와우')
elif cnt >= 3:
    print('이야')
else:
    print('이런')