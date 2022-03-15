str1 = 'BBQWORLD'
str2 = 'KFCAPPLE'
str3 = 'LOT'


target = input()

cnt = 0
for i in range(len(str1)):
    if str1[i] == target:
        cnt += 1
for i in range(len(str2)):
    if str2[i] == target:
        cnt += 1
for i in range(len(str3)):
    if str3[i] == target:
        cnt += 1

print(cnt)