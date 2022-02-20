a, b = input().split()

for j in range(4):
    for i in range(ord(a), ord(b)+1):
        print(chr(i), end = ' ')
    print()

