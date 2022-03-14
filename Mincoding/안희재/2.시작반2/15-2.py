num = int(input())

for i in range(4):
    a = num // (10 ** (3-i))
    num -= 10 ** (3-i) * a
    print(f'숫자{a}')

