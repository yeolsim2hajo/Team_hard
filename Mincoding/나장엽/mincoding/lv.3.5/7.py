# 변수 a, x를 만들고, 각 변수에 숫자를 입력 받아라
# a보다 작은 수를 x개 만큼 출력해라!


n1, n2 = map(int, input().split())

for i in range(n2):
    n1 -= 1
    print(n1, end=' ')
