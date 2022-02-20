arr = [['A','B','C'], ['A','G','H'], ['H','I','J'], ['K','A','B'], ['A','B','C']]

bucket = [0] * 26

for i in range(5):
    for j in range(3):
        index = ord(arr[i][j]) - 65
        bucket[index] += 1

answer = ''
for i in range(len(bucket)):
    if bucket[i] >= 1:
        answer += chr(i+65)*bucket[i]

print(answer)