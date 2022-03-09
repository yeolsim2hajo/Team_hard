a, b = input().split()
b = int(b)

MAP = [[3,5,4,2,2,3], [1,3,3,3,4,2], [5,4,4,2,3,5]]
price = ['T','P','G','K','C']

a2 = 0
if a == 'A':
    a2 = 0
elif a == 'B':
    a2 = 1
else:
    a2 = 2

print(price[MAP[a2][b-1]-1])
