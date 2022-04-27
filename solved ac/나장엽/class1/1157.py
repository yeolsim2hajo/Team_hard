target = list(input())


for i in range(len(target)):
    target[i] = target[i].upper()


dat = [0]*200
for i in range(len(target)):
    dat[ord(target[i])] += 1

Max = dat[0]
Max_idx = 0
for i in range(len(dat)):
    if Max < dat[i]:
        Max = dat[i]
        Max_idx = i


cnt = 0
for i in range(len(dat)):
    if Max == dat[i]:
        cnt += 1


if cnt > 1:
    print('?')
else:
    print(chr(Max_idx))