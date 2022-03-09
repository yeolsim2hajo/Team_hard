def sum(x,y):
    return x+y

def comp(x,y):
    return x-y

def Print(x,y):
    print(f'합:{x}')
    print(f'차:{y}')

def main():
    a, b = map(int,input().split())
    c = sum(a,b)
    d = comp(a,b)
    Print(c,d)

main()
