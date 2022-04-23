arr = []
for i in range(3):
    a, b = map(int,input().split())
    arr.append(a)

if sum(arr) == 3:
    print('안전')
else:
    print('위험')