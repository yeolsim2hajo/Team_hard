def mincoding():
    num = list(map(int,input().split()))
    return num

def main():
    a = mincoding()
    b = (f'({a[0]})({a[1]})')
    return b

print(main())