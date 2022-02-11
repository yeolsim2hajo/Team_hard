a = int(input())
b = int(input())

if b - a >= 31:
    print('You are speeding and your fine is $500.')
elif b - a >= 21:
    print('You are speeding and your fine is $270.')
elif b - a >= 1:
    print('You are speeding and your fine is $100.')
else:
    print('Congratulations, you are within the speed limit!')