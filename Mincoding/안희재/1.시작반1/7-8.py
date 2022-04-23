arr = [[3,4,1], [2,1,4], [3,3,0]]

even = 0
odd = 0
for i in range(3):
    for j in range(3):
        if arr[i][j] % 2:
            odd += 1
        else:
            even += 1

print(f'짝수 : {even}')
print(f'홀수 : {odd}')