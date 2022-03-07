arr = list(map(int,input().split()))

min = 2e18
max = 0
for i in arr:
    if i < min:
        min = i
    if i > max:
        max = i

print(f'MAX={max}')
print(f'MIN={min}')