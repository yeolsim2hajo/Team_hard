
def QTR():
    print('QTR100%')
    
def BBQ():
    print('BBQ100%')
    
arr = [0, 0, 0]
n = list(map(int, input().split()))

for i in range(len(n)):
    arr.append(n[i])
    
    
sum = 0
for k in range(len(arr)):
    sum += arr[k]


if sum >= 10:
    QTR()
else:
    BBQ()