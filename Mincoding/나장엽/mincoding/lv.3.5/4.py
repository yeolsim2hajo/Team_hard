# 숫자 하나를 입력받아라
# 규칙을 보고 For문을 이용해 값을 출력해라


# 입력 3
# 출력 5 6 7
# 입력 5
# 출력 7 8 9


n = int(input())

for i in range(3):
    n += 2
    print(n, end= ' ')
    n -= 1