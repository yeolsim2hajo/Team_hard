word = input()

for i in range(ord(word)-65+1):
    print(chr(i+65), end='')