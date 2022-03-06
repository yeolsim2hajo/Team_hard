n = int(input())
def BBQ(n):
    if 0 < n < 5:
        print('초기값')
    elif 6 < n < 10:
        print('중간값')
    else:
        print('알수없는값')
if n == 3 or n == 5 or n == 7:
    for i in range(1, 11, 1):
        print(i, end='')
elif n == 0 or n == 8:
    for i in range(10, 0, -1):
        print(i, end='')
else:
    BBQ(n)
    