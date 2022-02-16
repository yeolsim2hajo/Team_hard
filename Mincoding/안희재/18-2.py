a = [65000, 35, 42, 70, 70, 35, 65000, 1300, 65000, 30000, 38, 42]

bucket = [0] * 65535

for i in range(len(a)):
    index = a[i]
    bucket[index] += 1

# index = 65000, 35, 42, 70, 70, 35, 65000, 1300, 65000, 30000, 38, 42
# bucket[65000] = 0
max = 0
max_index = 0
for i in range(len(bucket)):
    if bucket[i] > max:
        max = bucket[i]
        max_index = i

print(max_index)
