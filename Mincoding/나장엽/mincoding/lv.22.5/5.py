#mapping

# 문자 2개를 입력받아라
# map 배열에서 찾을 값을 이용해 price 배열의 값을 찾아야한다
# 예를 들어 B3를 입력받았다면, map 배열에서 3을 찾을 수 있고, 
# price 배열의 3번에 해당하는 G를 출력하라.


board = [[3,5,4,2,2,3],[1,3,3,3,4,2],[5,4,4,2,3,5]]
price = ['T','P','G','K','C']

y, x = list(input().split())
x = int(x)
if y == 'A':
    y = 0
elif y == 'B':
    y = 1
else:
    y = 2

print(price[board[y][x-1]-1])