arr = input().split()

big = []
small = []

for i in arr:
    if i.isupper():
        big.append(i)
    if i.islower():
        small.append(i)

a = ''.join(big)
b = ''.join(small)

print(f'big={a}')
print(f'small={b}')