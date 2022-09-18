N = int(input())
numbers = list(map(int, input().split()))

cnt = 0
for number in numbers:
    flag = 0
    if number == 1:
        continue
    else:
        for i in range(2, number):
            if number %  i == 0:
                flag = 1
        if flag == 0:
            cnt += 1

print(cnt)