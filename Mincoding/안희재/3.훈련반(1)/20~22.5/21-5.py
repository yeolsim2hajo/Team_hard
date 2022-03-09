arr = [[input()] for i in range(3)]

max_word = ''
max_index = 0
for i in range(3):
    if len(max_word) < len(arr[i][0]):
        max_word = arr[i][0]
        max_index = i

arr[0], arr[max_index] = arr[max_index], arr[0]

for i in range(3):
    print(''.join(arr[i]))

# 어.. 재귀로 푸는건가..?