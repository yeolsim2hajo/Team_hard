# 최대 공약수와 최소 공배수

# 두 자연수를 입력받아 최대공약수와 최소 공배수를 출력
import sys
input = sys.stdin.readline

num1, num2 = map(int, input().split())
answer1 = []
if num1 > num2:
    for i in range(1, num2+1):
        if num1 % i == 0:
            if num2 % i == 0:
                answer1.append(i)

else:
    for i in range(1, num1+1):
        if num1 % i == 0:
            if num2 % i == 0:
                answer1.append(i)
n1 = max(answer1) # 최대공약수
n2 = int(num1/n1 * num2/n1)*n1 #최대공약수로 나눈 몫의 곱과 최대공약수를 곱하면 최고 공배수

print(n1)
print(n2)