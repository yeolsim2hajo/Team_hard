# 123456789를 입력받았으면 123,456,789 를 출력
n = input()
result = ''

for i in range(len(n)):
    if i == len(n)-1 and i % 3 == 2:
        result += n[i]
    elif i % 3 == 2:
        result += n[i] + ','
    else:
        result += n[i]

print(result)

# 엣..? format함수..
# n = int(input())

# result = format(n, ',')
# print(result)
