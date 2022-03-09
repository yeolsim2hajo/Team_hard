def QTR():
    print('QTR100%')

def BBQ():
    print('BBQ100%')

arr = list(map(int,input().split()))

sum = 0
for i in arr:
    sum += i

if sum >= 10:
    QTR()
else:
    BBQ()