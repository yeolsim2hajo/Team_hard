arr = list(input().split())


def chechChar(str):
    if ord('A') <= ord(str) <= ord('Z'):
        print('대', end='')
    else:
        print('소', end='')
        
for i in arr:
    chechChar(i)
    