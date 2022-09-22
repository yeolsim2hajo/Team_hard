import sys
input = sys.stdin.readline

lst = list(input().strip())
for i in range(len(lst)):
    if ord('a') <= ord(lst[i]) <= ord ('z'):
        lst[i] = chr(ord(lst[i])-32)
    else:
        lst[i] = chr(ord(lst[i])+32)
    print(lst[i], end="")