a, b, c = input().split()

def process():
    flag = 0
    if (a, b, c) == ('A', 'B', 'C'):
        flag = 1
    return flag

def output():
    process()
    if process() == 1:
        print('ABC를찾았다')
    else:
        print('못찾았다')

output()