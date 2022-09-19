# 백준 class 3++ 1463 1로 만들기

n = int(input())
lst = [0]*n
for i in range(1, n):
    rst = -1
    if i%3 == 0:
        rst = lst[i//3]+1
    elif i%2 == 0:
        rst = lst[i//2]+1
    else:
        lst[i] = lst[i-1]+1
    if rst != -1:
        if lst[i-1]+1 > rst:
            lst[i] = rst
        else:
            lst[i] = lst[i-1]+1

print(lst[n-1])