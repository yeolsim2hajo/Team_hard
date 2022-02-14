num1, num2 = map(int, input().split())

original_arr = [['A','B','C','D','E','F'],['G','H','I','J','K','L'],['M','N','O','P','Q','R']]

new_arr = [[0] * 3 for _ in range(6)]

for i in range(6):
    for j in range(3):
        new_arr[i][j] = original_arr[2-j][5-i]

print(new_arr[num1][num2])

# arr = [[''] * 3 for _ in range(6)]
# for x in range(2,-1,-1):
#     for y in range(5,-1,-1):
#         arr[y][x] = chr(ord('A')- 6*x - y + 17)

# a, b = list(map(int,input().split()))
# print(arr[a][b])
# 원경님 코드 - 네 번째 줄 한번에 짤 수 있겠는가!?