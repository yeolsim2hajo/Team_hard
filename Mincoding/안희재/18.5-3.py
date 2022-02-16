str = input()

bucket = [0] * 27

for i in range(len(str)):
    index = ord(str[i])-65
    bucket[index] += 1

max = 0
max_index = 0
for i in range(len(bucket)):
    if bucket[i] > max:
        max = bucket[i]
        max_index = i

print(chr(max_index+65))