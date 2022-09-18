str = list(input())
flag1 = 0
flag2 = 0
for i in range(0, len(str), 2):
    if ord('A') <= ord(str[i]) <= ord('Z'):
        flag1 += 1
for i in range(1, len(str), 2):
    if ord('a') <= ord(str[i]) <= ord('z'):
        flag2 += 1


if flag1 + flag2 == len(str):
    print('개구리문장')
else:
    print('일반문장')