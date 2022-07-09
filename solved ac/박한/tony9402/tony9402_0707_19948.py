# 백준 19948 음유시인 영재 - 틀렸습니다 뜸. 왜 ????

poem = list(input())
p = len(poem)
n = int(input())
lst = list(map(int, input().split()))
lst1 = [poem[0]]
check, rst, ans = n, 0, 0
def find_(m):
    while poem[m] == ' ' and m < p-1:
        m += 1
    lst1.append(poem[m])
    return m
    
def finda(m):
    ch = poem[m]
    while poem[m] == ch and m < p-1:
        m += 1
    return m
def findA(m):
    ch = poem[m]
    while poem[m] == ch and m < p-1:
        m += 1
    return m
while rst < p-1:
    if ord('A') <= ord(poem[rst]) <= ord('Z'):
        if lst[ord(poem[rst])-ord('A')] == 0:
            ans = -1
            break
        lst[ord(poem[rst])-ord('A')] -= 1
        rst = findA(rst)
    elif ord('a') <= ord(poem[rst]) <= ord('z'):
        if lst[ord(poem[rst])-ord('a')] == 0:
            ans = -1
            break
        lst[ord(poem[rst])-ord('a')] -= 1
        rst = finda(rst)
    else:
        if check == 0:
            ans = -1
            break
        check -= 1
        rst = find_(rst)
if poem[-1] != poem[-2]:
    if ord('A') <= ord(poem[-1]) <= ord('Z'):
        if lst[ord(poem[-1])-ord('A')] == 0:
            ans = -1
        else:
            if lst[-2] == ' ':
                lst1.append(poem[-1])
    else:
        if lst[ord(poem[-1])-ord('a')] == 0:
            ans = -1
        else:
            if lst[-2] == ' ':
                lst1.append(poem[-1])
if ans == -1:
    print(ans)
else:
    for i in range(len(lst1)):
        print(lst1[i].upper(), end="")