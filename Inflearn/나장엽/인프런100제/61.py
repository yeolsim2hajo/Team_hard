string = input()
target = string[0]
cnt = 0
result = ''
for i in string:
    if target == i:
        cnt += 1
    else:
        result += target + str(cnt)
        target = i
        cnt = 1


result += target+str(cnt)

print(result)