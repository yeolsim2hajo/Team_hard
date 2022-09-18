numbers = []

for i in range(10):
    numbers.append(int(input()))

result = []
for i in range(10):
    remain = numbers[i]%42
    result.append(remain)

result = set(result)

print(len(result))