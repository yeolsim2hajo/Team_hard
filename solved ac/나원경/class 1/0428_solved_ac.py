#2577 숫자의 개수
A = int(input())
B = int(input())
C = int(input())
result = str(A*B*C)
check = [0]*10
for num in result:
    check[int(num)] += 1
for i in range(10):
    print(check[i])