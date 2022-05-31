while True:
    numbers  = list(map(int, input().split()))
    if 0 in numbers:
        break
    Max = max(numbers)

    temp = 0
    for i in range(len(numbers)):
        if numbers[i] != Max:
            temp += numbers[i]**2

    if temp == Max**2:
        print('right')
    else:
        print('wrong')