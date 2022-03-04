arr = [["A","T","K","B"],["C","Z","F","D"], ["H","G","E","I"]]
str, x, y = list(input().split())
x, y = int(x), int(y)

#! arr의 모든 요소를 str과 비교, 
#! 비교값이 true이면 그 index부터 offset만큼 더하기
#! index+offset에 위치한 요소 출력하기


for row in range(3):
    for col in range(4):
        if arr[row][col] == str:
            print(arr[row+x][col+y])

