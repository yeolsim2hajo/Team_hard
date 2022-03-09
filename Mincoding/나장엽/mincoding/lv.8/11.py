price = int(input())
def starBox():
    for i in range(1, 21, 2):
        print(i, end= ' ')
def macDoll():
    for i in range(ord('H'), ord('A')-1, -1):
        print(chr(i), end= ' ')
def copyBean():
    for i in range(-5, 6, 1):
        print(i, end= ' ')


if 3500 < price <= 5000:
    starBox()
elif 2500 <= price < 3500:
    macDoll()
else:
    copyBean()
