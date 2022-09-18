
def BBQ(n):
    for i in range(1, n+1):
        print(i, end='')
def KFC(n):
    for i in range(7):
        print(n, end='')




n1 = int(input())
if n1 % 2 == 1:
    n2 = int(input())
    BBQ(n2)
else:
    str = input()
    KFC(str)