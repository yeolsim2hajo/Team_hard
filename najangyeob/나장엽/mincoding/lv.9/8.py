def main():
    a = list(map(int, input().split()))
    return a

def BBQ(a):
    print(f'합:{a[0]+a[1]}')
    print(f'차:{a[0]-a[1]}')
    print(f'곱:{a[0]*a[1]}')
    print(f'몫:{a[0]//a[1]}')


BBQ(main())