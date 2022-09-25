# 백준 1718 암호

import sys
input = sys.stdin.readline

lst = list(input().strip())
code = list(input().strip())
n, l, c = 0, len(lst), len(code)
while n < l:
    if lst[n] != ' ':
        a = (ord(code[n%c])-ord('a')+1)
        if (ord(lst[n])-a) < ord('a'):
            lst[n] = chr(ord(lst[n])-a+26)
        else:
            lst[n] = chr(ord(lst[n])-a)
    print(lst[n], end="")
    n += 1