str1 = list(input())
str2 = list(input())
flag=0
cnt = 0
for i in range(len(str1)-1, -1, -1):
    if str1[i] == str2[-i-1]:
        cnt += 1
        
if cnt == len(str1) :
    print('거울문장')
else:
    print('거울문장아님')