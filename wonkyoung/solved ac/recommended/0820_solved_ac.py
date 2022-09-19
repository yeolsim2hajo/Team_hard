#16927
import sys
new_input = sys.stdin.readline
N, M, R = map(int, new_input().split())
limit = min(N,M)//2

arr = [new_input().split() for _ in range(N)]

def rotate():
    global arr
    result = [[0]*M for _ in range(N)]
    for i in range(min(N,M)//2):
        for _ in range(R%(2*(N+M-2))):
            for row in {i, N-i-1}:
                edge = {i:1, N-i-1:-1}
                for col in range(M):
                    if (row,col) in {(i,i), (N-i-1,M-i-1)}:
                        result[row + edge[row]][col] = arr[row][col]
                    else:
                        result[row][col-edge[row]] = arr[row][col]
            for col in {i, M-i-1}:
                edge = {i: 1, M-i-1: -1}
                for row in range(N):
                    if row not in {i, N-i-1}:
                        result[row][col+edge[col]] = arr[row][col]
    return result
arr = rotate()
for i in range(N):
    print(*arr[i])

#4097 수익
# def calc_profit(arr, N):
#     if N == 2:
#         return max(arr[-1]-arr[0], arr[0], arr[-1])
#     if N == 1:
#         return arr[0]
#     half1, half2 = arr[:N//2], arr[N//2:]
#     profit1 = calc_profit(half1, N//2)
#     profit2 = calc_profit(half2, N - N//2)
#     min_profit, max_profit = arr[0], arr[N-1]
#     start, end = 0, N-1
#     while start <= end:
#         if min_profit > arr[start]:
#             min_profit = arr[start]
#         if max_profit < arr[end]:
#             max_profit = arr[end]
#         start += 1
#         end -= 1
#     return max(max_profit - min_profit, profit1, profit2)
#
# def input_profit():
#     import sys
#     new_input = sys.stdin.readline
#     while True:
#         N = int(new_input())
#         if N == 0:
#             return
#         profit_list=[(int(new_input()))]
#         for _ in range(N-1):
#             profit = profit_list[-1]+int(new_input())
#             profit_list.append(profit)
#         max_val = calc_profit(profit_list, N)
#         print(max_val)
#
# input_profit()


#1284 집 주소
def calc():
    import sys
    new_input = sys.stdin.readline
    while True:
        N = new_input().rstrip()
        if N == '0':
            return
        width = 1
        for i in N:
            if i == '1':
                width += 3
            elif i == '0':
                width += 5
            else:
                width += 4
        print(width)
calc()