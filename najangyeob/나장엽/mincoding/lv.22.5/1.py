arr = [
    [['A','T','B'],['C','C','B']],
    [['A','A','A'],['B','B','C']]
    ]

#arr의 index 0, 1/ 0, 1/ 0, 1

target = input()
result = 0
for i in range(2):
    for k in range(2):
        for j in range(3):
            if arr[i][k][j] == target:
                result = 1
                
if result :
    print('발견')
else:
    print('미발견')1