arr = [[3, 3, 5, 3, 1], [2, 2, 4, 2, 6], [
    4, 9, 2, 3, 4], [1, 1, 1, 1, 1], [3, 3, 5, 9, 2]]


def sum(arr):
    dy = [-1, -1, 1, 1]
    dx = [-1, 1, -1, 1]
    nx = 0
    ny = 0
    result = [[] for _ in range(5)]
    for row in range(5):
        for col in range(5):
            for j in range(4):
                sum = 0
                ny = dy[j] + ny
                nx = dx[j] + nx
                if 0 <= ny < 5 and 0 <= nx < 5:
                    sum = sum + arr[row][col] + arr[ny][nx]
                result[row].append(sum)
    max = result[0][0]
    x, y = 0, 0
    for k in range(5):
        for m in range(5):
            if max < result[k][m]:
                max = result[k][m]
                y = k
                x = m
        else:
            max = max
    return [x, y]


x = sum(arr)
print(x[0], x[1])


# arr을 순회하면서 특정 좌표값의 (ny, nx) 들의 합을 구하고, 가장 큰 값을 출력하는 함수
# arr[0][0] ~ arr[0][4]= 오아 밖에 없음
# arr[0][1] ~ arr[0][3]= 왼아, 오아
# 유효인덱스 범위 설정
# 0 <= nx < 5 and 0 <= ny < 5 일때만 ~~~~~~
# for j in range(4)
# sum = sum + arr[ny][nx]
# 값을 저장하는 result 리스트를 선언하고 for문으로 max값을 찾아서 출력
#

# 원경님 코드
# arr = ['33531','22426','49234','11111','33592']
# map_arr = [list(map(int,arr[i])) for i in range(5)]

# def sum(y,x):
#     dy = [-1,1,-1,1]
#     dx = [-1,1,1,-1]
#     sum_data = 0
#     for j in range(4):
#         if 0 <= y+dy[j] < 5 and 0 <= x+dx[j] < 5:
#             sum_data += map_arr[y+dy[j]][x+dx[j]]
#     return sum_data

# sum(1,2)

# max_data = 0
# for index in range(25):
#     if max_data < sum(index//5,index%5):
#         max_data = sum(index//5,index%5)
#         ans = index
# print(ans//5, ans%5)