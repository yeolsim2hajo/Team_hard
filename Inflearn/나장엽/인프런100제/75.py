'''
이상한 369
13 16은 x
36 39는 ok
'''

# 3-> 1 6 -> 2 9 -> 3 / 33 -> 4? (1+3)  36 -> 5? (2+3) 39 -> 6 (3+3)? / 63 -> 7 (1+6)


from itertools import product

user_input = '93'
listA = []
listB = []
count = 0

for i in range(1,len(user_input)+1) :
    listA+=list(product([3,6,9],repeat=i))


for i in listA :
    totalStr = ''
    for j in i :
        totalStr+=str(j)
    if int(user_input) >= int(totalStr) :
        count+=1

print(count)