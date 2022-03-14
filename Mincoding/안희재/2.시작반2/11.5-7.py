arr = [['a','b','d'], ['e','w','z'], ['q','v','a']]

def Input():
    word = input()
    return word

def process(x):
    a = x.lower()
    flag = 0
    for i in range(3):
        for j in range(3):
            if arr[i][j] == a:
                flag = 1
                return flag
    return flag

if process(Input()):
    print('존재')
else:
    print('없음')

