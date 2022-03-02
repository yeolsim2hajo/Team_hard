# 숫자 n을 입력받아라
# n부터 0까지 count down 했다가 다시 돌아오는 수를 출력해라
# 4 -> 4 3 2 1 0 1 2 3 4

n = int(input())
a = -n


def countdown(n):
    global a
    if n >= 0:
        print(n, end=' ')
        countdown(n-1)
    if  a <= n < 0:
        print(-n, end= ' ')
        countdown(n-1)


countdown(n)