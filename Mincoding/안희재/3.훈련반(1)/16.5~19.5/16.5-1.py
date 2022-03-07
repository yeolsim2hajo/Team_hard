a, b, c = map(int,input().split())

for i in range(c):
    for j in range(a,b+1):
        print(j, end = " ")
    print()