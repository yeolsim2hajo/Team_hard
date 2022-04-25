def plus(num) :
    sum = 0
    for i in num :
        sum+=int(i)
    return sum


#10 11 12 13 14 15 

s_num, e_num = map(int,input().split())
str1 = ''

for i in range(s_num,e_num+1) :
    str1 += str(i)

print(plus(str1))