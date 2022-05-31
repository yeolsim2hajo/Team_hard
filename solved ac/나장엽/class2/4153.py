while True:
    a, b, c = map(int, input().split())
    
    if a == 0 and b == 0 and c == 0:
        break
    else:
        num1 = a**2 + b**2

        if num1 == c**2 :
            print('right')
        else:
            print('wrong')