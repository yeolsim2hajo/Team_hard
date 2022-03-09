def main():
    a, b = map(int,input().split())

    def bbq(a,b):
        print(f'합:{a+b}')
        print(f'차:{a-b}')
        print(f'곱:{a*b}')
        print(f'몫:{a//b}')
    
    return bbq(a,b)

main()