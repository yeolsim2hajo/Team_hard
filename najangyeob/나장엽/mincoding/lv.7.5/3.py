def fn():
    n = list(input().split())
    return n

def output(n):
    if n[0].isupper() and n[1].isupper() == True:
        print('대문자들')   
    elif n[0].isupper() or n[1].isupper() == True:
        print('대소문자')
    else:
        for i in range(ord('a'), ord('z')+1, 1):
            print(chr(i), end='')
            
output(fn())