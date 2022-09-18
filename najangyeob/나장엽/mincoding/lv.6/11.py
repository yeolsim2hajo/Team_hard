str1, str2 = input().split()

for k in range(4):
    for i in range(ord(str1), ord(str2)+1):
        print(chr(i), end= ' ')
    print()