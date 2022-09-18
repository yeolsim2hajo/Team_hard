path = ['']*3
sign = ['A','B','C','D']

str = list(input())

result = []
def abc(level):
    if level == 3:
        result.extend(path)     
        return
    for i in range(4):
        path[level] = sign[i]
        abc(level+1)
    return result

abc(0)

result2 = []
for i in range(0, len(result), 3):
    result2.append(result[i:i+3])

for i in range(0, len(result2), 1):
    if str == result2[i]:
        print(f'{i+1}번째')