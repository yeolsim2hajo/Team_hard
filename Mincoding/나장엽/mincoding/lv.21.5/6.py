arr = [
    [1,5,3],
    [4,5,5],
    [3,3,5],
    [4,6,2]
]

a, b = map(int, input().split())

# a, b사이에 있는 숫자들을 모두 0으로 바꿔라..
# 출력할때 0 인 부분은 #으로 바꾸라..


for i in range(4):
    for k in range(3):
        if a<= arr[i][k] <= b :
            arr[i][k] = 0
for i in range(4):
    for k in range(3):
        if arr[i][k] == 0:
            print('#', end = ' ')
        else:
            print(arr[i][k], end = ' ')
    print()