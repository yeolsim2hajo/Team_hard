str1 = 'ATKPTCABC'
str2 = input().split()

idx1 = 0
for i in range(len(str1)):
    if str1[i] == str2[0]:
        idx1 = i
        break

for i in range(len(str1)-1,-1,-1):
    if str1[i] == str2[1]:
        idx2 = i
        break

print(abs(idx1-idx2))