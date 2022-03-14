arr = input().split()

def checkChar():
    for i in arr:
        if i.isupper() == 1:
            print('대',end='')
        if i.islower() == 1:
            print('소',end='')

checkChar() 