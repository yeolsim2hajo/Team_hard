arr = [3,7,4,1,2,6]
univer = []

for i in range(2):
    lst = list(map(int, input().split()))
    univer.append(lst)

def isExist(num):
    result = 0
    for i in arr:
        if num == i:
            result = 1
    return result

for i in range(2):
    for j in range(2):
        if isExist(univer[i][j]):
            univer[i][j] = 'OK'
        else:
            univer[i][j] = 'NO'

print(' '.join(univer[0]))
print(' '.join(univer[1]))


