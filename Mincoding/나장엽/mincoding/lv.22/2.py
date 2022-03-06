a = list(input())
b = list(input())
c = list(input())


if a == b == c :
    print('WOW')
elif a == b or b == c or a == c:
    print('GOOD')
else:
    print('BAD')