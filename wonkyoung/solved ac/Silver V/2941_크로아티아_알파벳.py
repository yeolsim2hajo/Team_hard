#220921
word = input()
length = len(word)
index = 0
croatia = {'c' : {'=', '-'},
           'd' : {'-'},
           'l' : {'j'},
           'n' : {'j'},
           's' : {'='},
           'z' : {'='}
           }
cnt = 0
while index < length:
    if word[index:index+3] == 'dz=':
        index += 2
    elif index + 1 != length and word[index+1] in croatia.get(word[index], ''):
        index += 1
    cnt += 1
    index += 1
print(cnt)


# 함수로 만들기
def plug():
    word = input()
    length = len(word)
    index = 0
    croatia = {'c': {'=', '-'},
               'd': {'-'},
               'l': {'j'},
               'n': {'j'},
               's': {'='},
               'z': {'='}
               }
    cnt = 0
    while index < length:
        if word[index:index + 3] == 'dz=':
            index += 2
        elif index + 1 != length and word[index + 1] in croatia.get(word[index], ''):
            index += 1
        cnt += 1
        index += 1
    return cnt
print(plug())


# in
def plug():
    word = input()
    length = len(word)
    index = 0
    croatia = {'c=', 'c-', 'd-','lj', 'nj', 's=', 'z='}
    cnt = 0
    while index < length:
        if word[index:index+2] in croatia:
            index += 1
        elif word[index:index+3] == 'dz=':
            index += 2
        cnt += 1
        index += 1
    return cnt
print(plug())
