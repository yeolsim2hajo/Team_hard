while True:
    number = input().strip()
    if number == '0':
        break
    number = number[::-1]
    total = 0
    for num in number:
        total += int(num)
    print(int(number), total)

