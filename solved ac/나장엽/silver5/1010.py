# n <= M
# 최대 연결할 수 있는 다리의 개수는 n개
# m개의 지역에 n개의 다리를 놓을 수 있는 경우의 수를 구하는 문제
# mCn으로 표현 -> m! 을 (m-n)!n!으로 나눈 값

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    bridge = factorial(n) // (factorial(n) * factorial(m - n))
    print(bridge)