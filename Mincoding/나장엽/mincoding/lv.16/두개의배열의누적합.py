arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))


temp = arr_a + arr_b
result = list()


for i in range(0, 4):
    result.append(temp[i] + temp[-i-1])

for i in result:
    print(i, end=' ')