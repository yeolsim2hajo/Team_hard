# 백준 9012 괄호

T = int(input())
for _ in range(T):
    lst = list(input())
    rst = 0
    for i in range(len(lst)):
        if rst < 0:
            break
        if lst[i] == ')':
            rst -= 1
        else:
            rst += 1
    if rst == 0:
        print("YES")
    else:
        print("NO")