# 길이가 n인 정수 배열 a와 b가 있다.
# 함수 s
# a[0]*b[0] + ..... a[n-1]*b[n-1]
# s의 값을 가장 작게 만들기 위해 a의 수를 재배열해라.
# s의 최솟값을 출력해라.

# b 배열은 건드리지 않고, a 배열만 건드려서 함수 s의 최솟값을 구해야한다.
# b 배열을 중 가장 큰 수와 a의 가장 작은 수를 곱하면 최솟값이 나온다.
# 1 1 1 6 0 / 2 7 8 3 1 
# 1 1 1 6 0/ 1 2 3 7 8 -> 6 + 2 + 3 + 7 + 0 => 18
# 1 1 3 / 10 30 20 -> 1 x 30, 1 x 20, 3 x 10 => 80


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


acc = 0
for i in range(N):
    acc += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))

print(acc)