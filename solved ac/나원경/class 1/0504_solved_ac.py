#1018 체스판 다시 칠하기
# N, M = map(int,input().split())
# chess = [input() for _ in range(N)]
# min_cnt = 64
# for i in range(N-7):
#     for j in range(M-7):
#         pass

#1085 직사각형에서 탈출
# x, y, w, h = map(int, input().split())
# print(min(x, w-x, y, h-y))

# class 1
#10951 A+B - 4
while 1:
    try:
        A, B = map(int,input().split())
        print(A+B)
    except EOFError:
        break