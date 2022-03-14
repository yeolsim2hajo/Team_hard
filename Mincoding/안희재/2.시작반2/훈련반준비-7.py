a1 = []
b1 = 0
c1 = 0
for i in range(2):
    a = input()
    b = int(input())
    c = int(input())
    a1.append(a)
    b1 += b
    c1 += c

print(f'{a1[0]},{a1[1]}')
print(f'AverageSize={b1//2}')
print(f'AveragePrice={c1//2}')
