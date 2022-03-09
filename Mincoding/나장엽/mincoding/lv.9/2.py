arr = [['A','B','C','D','E'],['E','A','B','A','B'],['A','C','D','E','R']]

str = input()
cnt = 0
for i in range(3):
    for k in range(5):
        if arr[i][k] == str:
            cnt += 1
            

if cnt >= 3:
    print('대발견')
elif 1 <= cnt <= 2:
    print('발견')
else:
    print('미발견')