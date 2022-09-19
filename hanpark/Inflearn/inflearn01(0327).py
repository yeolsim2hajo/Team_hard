# codeFestival_1. 92번

lst = list(input().split())
m = ['0']*len(lst[1])
n = ['0']*len(lst[1])
for i in range(len(lst[1])):
    if lst[1][i] == '3':
        m[i] = '1'
        n[i] = '2'
    elif lst[1][i] == '4':
        m[i] = '2'
        n[i] = '2'
    elif lst[1][i] == '6':
        m[i] = '1'
        n[i] = '5'
    else:
        m[i] = '0'
        n[i] = lst[1][i]

lst1 = ['']*4
lst2 = ['']*4
for i in range(4):
    lst1[i] = lst[i]
    lst2[i] = lst[i]

m1, n1 = '', ''
for i in range(len(lst[1])):
    m1 += m[i]
    n1 += n[i]
lst1[1], lst2[1] = m1, n1

print(lst1)
print(lst2)