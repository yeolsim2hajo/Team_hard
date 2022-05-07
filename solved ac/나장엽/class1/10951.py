while True:
    try:
        number1, number2 = map(int, input().split())
        Sum = number1 + number2
        print(Sum)
    except:
        break