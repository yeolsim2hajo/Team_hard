n = int(input())
temp = n
for i in range(4):
    n = temp
    n -= i
    for k in range(4):
        print(n, end='')
    print()
