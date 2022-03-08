def printData(x):
    print(x)

def even(x,y):
    return printData(x//y * 2)

def odd(x,y):
    return printData(x//y - 10)

def main():
    a, b = map(int,input().split())
    if (a//b) % 2 == 0:
        even(a,b)
    else:
        odd(a,b)
    
    printData(a+b)

main()