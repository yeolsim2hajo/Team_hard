a, b, c = input().split()

a = int(a)
b = int(b)

for i in range(3):
    if i == 1:
        print()
    else:
        for j in range(a):
            for k in range(b):
                print(c, end = "")
            print()