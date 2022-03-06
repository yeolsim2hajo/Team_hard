a = int(input())

def BBQ(x):
    if 0 < x < 5:
        print('초기값')
    elif 6 < x < 10:
        print('중간값')
    else:
        print('알수없는값')

if a == 3 or a == 5 or a == 7:
    for i in range(1,11):
        print(i,end='')
elif a == 0 or a == 8:
    for i in range(10,0,-1):
        print(i,end='')
else:
    BBQ(a)