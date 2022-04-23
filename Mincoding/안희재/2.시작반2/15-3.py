num = list(map(int,input().split()))

result = '완벽한배치'
for i in range(5):
    if abs(num[i] - num[i+1]) >= 3:
        result = '재배치필요'
        print(result)
        break
else:
    print(result)