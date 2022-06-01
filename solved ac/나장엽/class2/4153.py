while True:
    numbers  = list(map(int, input().split()))
    if 0 in numbers: # 종료조건
        break


    Max = max(numbers) # 가장 큰 변의 길이 
    temp = 0 
    for i in range(len(numbers)):
        if numbers[i] != Max: # 가장 큰 변의 길이를 제외한 나머지 변들을 제곱하고, 더함
            temp += numbers[i]**2

    if temp == Max**2: # 직각삼각형의 조건을 만족하면
        print('right')
    else:
        print('wrong')

# 반례 5 3 4 
# a^2 + b^2 = c^2
