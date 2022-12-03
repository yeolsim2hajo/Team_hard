# 백준 1718 암호

import sys
input = sys.stdin.readline

a=input()
b=input()
for i in range(len(a)):
    if a[i]==' ': print(" ",end='')
    else:
        if ord(a[i])-ord(b[i%len(b)])<=0:
            print(chr(ord(a[i]) - ord(b[i%len(b)]) +26+ 96), end='')
        else :print( chr(ord(a[i])-ord(b[i%len(b)])+96 ), end='' )