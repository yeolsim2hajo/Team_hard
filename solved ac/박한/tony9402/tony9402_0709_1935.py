# 백준 1935 후위 표기식2

n = int(input())
ls = list(input())
lst = [int(input()) for _ in range(n)]
ans = []
for i in range(len(ls)):
    if ord('A') <= ord(ls[i]) <= ord('Z'):
        ans.append(lst[ord(ls[i])-ord('A')])
    else:
        a = ans.pop()
        b = ans.pop()
        if ls[i] == '+':
            ans.append(a+b)
        elif ls[i] == '-':
            ans.append(b-a)
        elif ls[i] == '*':
            ans.append(a*b)
        else:
            ans.append(b/a)
print(f"{ans[0]:.2f}")