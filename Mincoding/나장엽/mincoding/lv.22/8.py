arr = [
        [[2,4],[1,5]],
        [[2,3],[3,6]],
        [[7,3],[1,5]]
    ]
# arr[0], arr[1], arr[2]
n = int(input())
cal_arr = arr[n] # n=1 일때, [[2,3],[1,5]]


max = cal_arr[0][0]
min = cal_arr[0][0]

for row in range(2):
    for col in range(2):
        # 배열의 max 깂 구하기
        if max < cal_arr[row][col]:
            max = cal_arr[row][col]
        else:
            max = max
            
        # 배열의 min 값 구하기    
        if min > cal_arr[row][col]:
            min = cal_arr[row][col]
        else:
            min = min
            
print(f'MAX={max}')
print(f'MIN={min}')