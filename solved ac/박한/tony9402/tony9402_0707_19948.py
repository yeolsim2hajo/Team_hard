# 백준 19948 음유시인 영재

import sys
input = sys.stdin.readline
poem = input()
p = len(poem)
n = int(input())
lst = list(map(int, input().split()))
lst1 = [lst[0]]
check, rst, ans = n, 0, 0
def find_(m):
    while lst[m] == ' ' and m < n-1:
        m += 1
    lst.append(lst[m])
    return m
    
def finda(m):
    ch = lst[m]
    while lst[m] == ch and m < n-1:
        m += 1
    return m
def findA(m):
    ch = lst[m]
    while lst[m] == ch and m < n-1:
        m += 1
    return m
while rst < n-1:
    if ord('A') <= ord(lst[rst]) <= ord('Z'):
        if lst[ord(lst[rst])-ord('A')] == 0:
            ans = -1
            break
        lst[ord(lst[rst])-ord('A')] -= 1
        rst = findA(rst)
    elif ord('a') <= ord(lst[rst]) <= ord('z'):
        if lst[ord(lst[rst])-ord('a')] == 0:
            ans = -1
            break
        lst[ord(lst[rst])-ord('a')] -= 1
        rst = finda(rst)
    else:
        if check == 0:
            ans = -1
            break
        check -= 1
        rst = find_(rst)
if lst[-1] != lst[-2]:
    if ord('A') <= ord(lst[-1]) <= ord('Z'):
        if lst[ord(lst[-1])-ord('A')] == 0:
            ans = -1
        else:
            if lst[-2] == ' ':
                lst1.append(lst[-1])
    else:
        if lst[ord(lst[-1])-ord('a')] == 0:
            ans = -1
        else:
            if lst[-2] == ' ':
                lst1.append(lst[-1])
if ans == -1:
    print(ans)
else:
    lst1.upper()
    for i in range(len(lst1)):
        print(lst1[i], end="")