# 숫자 하나를 입력받고, 입력받은 값부터 0 까지 출력해주세요

n = int(input())

for i in range(n, -1, -1):
    print(i, end='')