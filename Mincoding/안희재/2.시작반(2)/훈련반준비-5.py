a, b, c = map(int,input().split())

for i in range(c):
    for j in range(a,a+b):
        print(j, end=' ')
    print()