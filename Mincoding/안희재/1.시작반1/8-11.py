price = int(input())

def starBox():
    for i in range(1,20,2):
        print(i,end= ' ')

def macDoll():
    arr = ['A','B','C','D','E','F','G','H']
    print(*arr[::-1])

def copyBean():
    for i in range(-5,6):
        print(i,end=' ')

if 3500 <= price <= 5000:
    starBox()
elif price < 3500:
    macDoll()
else:
    copyBean()