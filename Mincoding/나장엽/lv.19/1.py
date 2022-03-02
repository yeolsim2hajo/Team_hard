a = [[3,5,4], [1,1,2], [1,3,9]]

# 입력받을 좌표값.
y, x = list(map(int, input().split()))

# top bottom left right
directy = [-1, 1, 0, 0]
directx = [0, 0, -1, 1]

result = 0

for i in range(4):
    dy = directy[i] + y
    dx = directx[i] + x

# 좌표값이 유효하지 않다면? 0,0 일경우 top과 left가 없음..

    if 0 <= dy < 3 and 0 <= dx < 3:       
        result += a[dy][dx]

        
print(result)