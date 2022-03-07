# 음.. direct쓰는 문제가 아니라고?
# how to solve? 아 그냥 반복문으로??

image = []

for i in range(4):
    nums = list(map(int,input().split()))
    image.append(nums)

def rectSum(x,y): # x는 행, y는 열
    sum = 0
    for i in range(2):
        for j in range(3):
            if 0<= x+i < 4 and 0 <= y+j < 4:
                sum += image[x+i][y+j]
    return sum

max = 0
a, b = (0,0)
for i in range(4):
    for j in range(4):
        if rectSum(i,j) > max:
            max = rectSum(i,j)
            a,b = (i,j)

print(f'({a},{b})')

