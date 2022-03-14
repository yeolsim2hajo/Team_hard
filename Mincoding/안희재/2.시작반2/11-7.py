arr = list(map(int,input().split()))

min = 2e18
max = 0
for i in arr:
    if min > i:
        min = i
    if max < i:
        max = i

print(f'MAX={max}')
print(f'MIN={min}')

