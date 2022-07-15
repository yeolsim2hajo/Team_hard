# 백준 1972 놀라운 문자열

def abc(n):
    m = len(n)
    if m <= 2:
        return 1
    check = 1
    while check <= m-1:
        lst = []
        for i in range(m-check):
            ans = n[i]+n[i+check]
            if ans in lst:
                return 0
            else:
                lst.append(ans)
        check += 1
    return 1

while 1:
    a = input()
    if a == '*':
        break
    rst = abc(a)
    if rst == 1:
        print(f"{a} is surprising.")
    else:
        print(f"{a} is NOT surprising.")