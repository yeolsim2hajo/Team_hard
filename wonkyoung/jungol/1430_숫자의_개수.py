#221111
result = 1
for _ in range(3):
    result *= int(input())
result = str(result)
check = [0] * 10
for i in result:
    check[int(i)] += 1
print(*check, sep='\n')