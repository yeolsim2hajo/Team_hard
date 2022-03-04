arr = [[3,1,9],[7,2,1,],[1,0,8]]
mask = [list(map(int, input().split()))for _ in range(3)]

def find(arr, mask):
    masked_arr = [[0,0,0],[0,0,0],[0,0,0]]

    # 마스캉하는 함수
    for row in range(3):
        for col in range(3):
            if mask[row][col] == 1:
                masked_arr[row][col] = arr[row][col]
    # 존재하는지 안하는지 찾는 함수 작성하기
    result = 0
    for r in range(3):
        for c in range(3):
            if 3 <= masked_arr[r][c] <= 5:
                result = 1

    return result

if find(arr, mask) == 1:
    print("발견")
else:
    print("미발견")