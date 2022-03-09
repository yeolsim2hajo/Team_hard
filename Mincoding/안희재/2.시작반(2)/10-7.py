def GOP():
    a, b = map(int,input().split())
    return a * b

def SUM():
    a, b = map(int,input().split())
    return a + b

def main():
    c = GOP()
    d = SUM()
    if c > d:
        print('GOP>SUM')
    elif c < d:
        print('GOP<SUM')
    else:
        print('GOP==SUM')

main()