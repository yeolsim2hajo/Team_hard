a, b, c = map(int, input().split())


max = 0
min = 0


if a >= b and b >= c:
    max = a
    min = c
elif b >= a and b >= c:
    max = b
else:
    max = c

if a <= b and b <= c:
    min = a
elif b <= a and b <= c:
    min = b
else:
    min = c
    
print(f'MAX={max}')
print(f'MIN={min}')