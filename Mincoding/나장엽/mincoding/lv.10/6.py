def main():
    a, b = map(int, input().split())
    if int(a/b)%2 == 0:
        even(int(a/b))    
    else:
        odd(int(a/b))
    printData(a+b)
    
def even(n):
    n = n*2
    printData(n)
    
def odd(n):
    n = n - 10
    printData(n)

def printData(n):
    print(n)
    
main()