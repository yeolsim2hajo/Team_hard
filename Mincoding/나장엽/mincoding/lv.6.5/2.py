str = input()


for i in range(ord(str), ord('a')-1, -1):
    print(chr(i), end='')