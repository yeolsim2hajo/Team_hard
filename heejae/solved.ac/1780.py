import sys

N = int(sys.stdin.readline())
matrix = []
result = [0, 0, 0]

for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))


def count(start_x: int, start_y: int, n: int):
    temp = matrix[start_x][start_y]
    rtn = [0, 0, 0]
    for i in range(n):
        for j in range(n):
            if temp != matrix[start_x + i][start_y + j]:
                rtn = divide(start_x, start_y, n)
                return rtn

    rtn[temp + 1] += 1
    return rtn



def divide(start_x: int, start_y: int, n: int):
    result = [0, 0, 0]
    temp = []
    
    for i in range(3):
        for j in range(3):
            temp = count(start_x + i* n//3, start_y + j* n//3, n//3)
            result[0] += temp[0]; result[1] += temp[1]; result[2] += temp[2]

    return result


result = count(0, 0, N)
print(result[0])
print(result[1])
print(result[2])
출처: https://suri78.tistory.com/69 [공부노트:티스토리]