a, b = map(int,input().split())

if a > b:
    if (a - b) % 2:
        print('고백한다')
    else:
        print('짝사랑만')
else:
    if (b - a) % 2:
        print('고백한다')
    else:
        print('짝사랑만')