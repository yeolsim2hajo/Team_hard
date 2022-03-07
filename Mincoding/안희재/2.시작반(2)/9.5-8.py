num = int(input())

if num % 2:
    num2 = int(input())
    def BBQ(num2):
        for i in range(1,num2+1):
            print(i,end='')
    BBQ(num2)

else:
    str = input()
    def KFC(str):
        for i in range(7):
            print(str,end='')
    KFC(str)