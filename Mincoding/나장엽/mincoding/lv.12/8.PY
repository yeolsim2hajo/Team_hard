arr = ['D','A','T','A','P','O','W','E','R']

a, b = map(int, input().split())

temp = [0]*9
for k in range(len(temp)):
    temp[k] = arr[a]
    if a >=b:
        break
    a += 1

for i in range(len(temp)):
    if temp[i] == 0:
        print(' ', end='')
    else:
        print(temp[i], end='')