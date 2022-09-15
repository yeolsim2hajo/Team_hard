# n은 a의 배수, a는 1과 n이 아니다
# n을 구하라

# n의 진짜 약수 개수가 주어진다.
# 2번째 줄에 n의 진짜 약수가 주어진다.


cnt = int(input())
number = list(map(int, input().split()))
a = min(number)
b = max(number)
print(a * b)

