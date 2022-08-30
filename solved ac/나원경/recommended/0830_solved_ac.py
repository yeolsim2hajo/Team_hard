#1932 정수 삼각형 (실버1)
def find_max():
    N = int(input())
    if N == 1:
        return int(input())
    triangle = [list(map(int, input().split())) for _ in range(N)]
    for i in range(2):
        triangle[1][i] += triangle[0][0]
    for j in range(2,N):
        for i in range(j+1):
            if i == 0:
                triangle[j][i] += triangle[j-1][i]
            elif i == j:
                triangle[j][i] += triangle[j-1][i-1]
            else:
                triangle[j][i] += max(triangle[j-1][i-1], triangle[j-1][i])
    return max(triangle[-1])
print(find_max())