a = list(input() for _ in range(4))

result = []
for i in range(4):
    result.append(len(a[i]))



max = result[0]
min = result[0]
max_idx = 0
min_idx = 0

for i in range(len(result)):
    if max < result[i]:
        max = result[i]
        max_idx = i
    else:
        max = max
    if min > result[i]:
        min = result[i]
        min_idx = i
    else:
        min = min 

print(f'긴문장:{max_idx}')
print(f'짧은문장:{min_idx}')