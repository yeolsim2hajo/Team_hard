a, b, c = map(int, input().split())

for i in range(c):
    for k in range(a, b+1):
        print(k, end=' ')
    print()