arr = [['G','K','T'], ['P','A','C']]
str = input().split()

def isExist(lst):
    result = 0
    for i in range(len(lst)):
        for j in range(2):
            for k in range(3):
                if str[i] == arr[j][k]:
                    result += 1
    return result

if isExist(str) == 0:
    print('미발견')
elif isExist(str) == 1:
    print('중발견')
else:
    print('대발견')
