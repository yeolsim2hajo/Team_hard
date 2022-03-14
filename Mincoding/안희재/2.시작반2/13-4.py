def ABC(x,y):
    SUM = x+y
    GOP = x*y
    print(SUM, GOP)

def main():
    a, b = map(int,input().split())
    return ABC(a,b)

main()