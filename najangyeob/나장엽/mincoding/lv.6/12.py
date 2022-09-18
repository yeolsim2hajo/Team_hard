a, b, c = input().split()


def process(a, b, c):
    flag = 0
    if a == 'A' and b == 'B' and c == 'C':
        flag = 1
    return flag
    
    
def output(x):
    if x == 1:
        print('ABC를찾았다')
    else:
        print('못찾았다')
        
        
output(process(a, b, c))