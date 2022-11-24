# tony9402 5397 키로거

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    A = input().strip()
    lst1, lst2 = [], []
    for a in A:
        if a == '<':
            if lst1:
                lst2.append(lst1.pop())
        elif a == '>':
            if lst2:
                lst1.append(lst2.pop())
        elif a == '-':
            if lst1:
                lst1.pop()
        else:
            lst1.append(a)
    lst1.extend(reversed(lst2))
    print(''.join(lst1))